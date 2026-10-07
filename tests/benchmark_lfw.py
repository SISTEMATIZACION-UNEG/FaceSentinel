#!/usr/bin/env python3
"""
benchmark_lfw.py — Validación biométrica masiva sobre el dataset estándar LFW (ISO/IEC 19795-1)
Proyecto: FaceSentinel

Métricas y evaluaciones:
1. Reutilización directa del extractor de embeddings (ArcFace 512-d) de FaceSentinel.
2. Comparación de umbrales:
   - Umbral de la literatura (d < 0.68)
   - Umbral calibrado FaceSentinel (d < 0.60, settings.FACE_MATCH_THRESHOLD)
3. Métricas biométricas ISO/IEC 19795-1:
   - Exactitud global (Accuracy)
   - FMR (False Match Rate / Falsa Aceptación)
   - FNMR (False Non-Match Rate / Falso Rechazo)
   - EER (Equal Error Rate) y AUC de la curva ROC
4. Prueba de estrés 1:N en ChromaDB:
   - Instancia aislada en memoria (EphemeralClient) con métrica coseno indexada por HNSW.
   - Enrolamiento de 1.000 identidades sintéticas.
   - Medición de latencia media y P95 en milisegundos de 50 consultas de similitud.
5. Exportación de resultados a JSON en `data/lfw_benchmark_results.json` y consola formateada.
"""

import os
import sys
import time
import json
import logging
import argparse
from datetime import datetime
from pathlib import Path

import cv2
import numpy as np

# Configurar ruta base del proyecto para importar módulos de FaceSentinel
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Silenciar advertencias irrelevantes de TensorFlow/OneDNN para mantener la consola limpia
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Importar servicios de FaceSentinel
try:
    from app.services.face_recognition import get_embedding
    from app.core.config import settings
except ImportError as err:
    print(f"[ERROR] No se pudieron importar los servicios de FaceSentinel: {err}")
    print("Asegúrate de ejecutar el script desde el entorno virtual del proyecto.")
    sys.exit(1)

import chromadb
from sklearn.datasets import fetch_lfw_pairs
from sklearn.metrics import roc_curve, auc, roc_auc_score


# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("LFW_Benchmark")


# =========================================================================
#                    PREPROCESAMIENTO Y NORMALIZACIÓN
# =========================================================================

def preprocess_lfw_image(img_raw: np.ndarray) -> np.ndarray:
    """
    Adapta una imagen del dataset LFW al pipeline de visión artificial de FaceSentinel.
    
    LFW en scikit-learn provee arreglos float32 en rango [0.0, 1.0] con canales RGB.
    El motor de FaceSentinel (OpenCV + MediaPipe + DeepFace) requiere arreglos
    uint8 en rango [0, 255] con codificación de color BGR.
    """
    if img_raw is None or img_raw.size == 0:
        return None

    # 1. Escalar de float [0.0, 1.0] a uint8 [0, 255] si es necesario
    if img_raw.dtype != np.uint8:
        img_uint8 = np.clip(img_raw * 255.0, 0, 255).astype(np.uint8)
    else:
        img_uint8 = img_raw.copy()

    # 2. Conversión de espacio de color RGB -> BGR
    if len(img_uint8.shape) == 3 and img_uint8.shape[2] == 3:
        img_bgr = cv2.cvtColor(img_uint8, cv2.COLOR_RGB2BGR)
    elif len(img_uint8.shape) == 2:
        img_bgr = cv2.cvtColor(img_uint8, cv2.COLOR_GRAY2BGR)
    else:
        img_bgr = img_uint8

    # 3. Adecuación de escala si la imagen proviene del recorte por defecto de sklearn (62x47)
    # Reescalar a resolución nativa (250x250) permite que el detector de rostros opere
    # sobre el rostro sin perder rasgos por resolución subcrítica.
    h, w = img_bgr.shape[:2]
    if h < 112 or w < 112:
        img_bgr = cv2.resize(img_bgr, (250, 250), interpolation=cv2.INTER_CUBIC)

    return img_bgr


def l2_normalize(vector: list | np.ndarray) -> np.ndarray:
    """Normaliza un vector de características a norma L2 unitaria."""
    v = np.asarray(vector, dtype=np.float32)
    norm = np.linalg.norm(v)
    if norm > 0:
        return v / norm
    return v


def compute_cosine_distance(u: list | np.ndarray, v: list | np.ndarray) -> float:
    """
    Calcula la distancia coseno métrica d(u, v) = 1 - (u · v)
    para vectores normalizados en norma L2, exactamente como lo indexa ChromaDB en HNSW.
    """
    u_norm = l2_normalize(u)
    v_norm = l2_normalize(v)
    dot_prod = float(np.dot(u_norm, v_norm))
    dot_prod = max(-1.0, min(1.0, dot_prod))
    return float(1.0 - dot_prod)


# =========================================================================
#                    MÉTRICAS ISO/IEC 19795-1
# =========================================================================

def calculate_iso_metrics(distances: np.ndarray, labels: np.ndarray, threshold: float) -> dict:
    """
    Calcula las métricas de rendimiento bajo el estándar ISO/IEC 19795-1
    para un umbral de decisión específico d(u, v) < threshold.
    
    - labels: 1 para pares genuinos (misma persona), 0 para impostores (personas distintas).
    - distances: distancia coseno d ∈ [0, 2]. Menor distancia = mayor similitud.
    
    Decisión:
      - Match (Positivo) si d < threshold
      - Non-Match (Negativo) si d >= threshold
    """
    # Predicciones binarias: True si el sistema decide que es la misma persona
    predictions = distances < threshold

    # Conteo de transacciones
    genuine_mask = (labels == 1)
    impostor_mask = (labels == 0)

    n_genuine = int(np.sum(genuine_mask))
    n_impostor = int(np.sum(impostor_mask))
    n_total = len(labels)

    # True Matches (Genuinos aceptados)
    true_matches = int(np.sum(predictions[genuine_mask]))
    # False Non-Matches (Genuinos rechazados por error) -> FNMR
    false_non_matches = n_genuine - true_matches

    # False Matches (Impostores aceptados por error) -> FMR
    false_matches = int(np.sum(predictions[impostor_mask]))
    # True Non-Matches (Impostores rechazados correctamente)
    true_non_matches = n_impostor - false_matches

    # Tasas
    accuracy = (true_matches + true_non_matches) / n_total if n_total > 0 else 0.0
    fmr = false_matches / n_impostor if n_impostor > 0 else 0.0
    fnmr = false_non_matches / n_genuine if n_genuine > 0 else 0.0

    return {
        "threshold": float(threshold),
        "accuracy": float(accuracy),
        "accuracy_pct": float(accuracy * 100.0),
        "fmr": float(fmr),
        "fmr_pct": float(fmr * 100.0),
        "fnmr": float(fnmr),
        "fnmr_pct": float(fnmr * 100.0),
        "confusion_matrix": {
            "true_matches": true_matches,
            "false_non_matches": false_non_matches,
            "false_matches": false_matches,
            "true_non_matches": true_non_matches,
            "total_genuine": n_genuine,
            "total_impostor": n_impostor
        }
    }


def compute_roc_and_eer(distances: np.ndarray, labels: np.ndarray) -> dict:
    """
    Calcula la curva ROC, el área bajo la curva (AUC) y el Equal Error Rate (EER).
    
    Dado que las distancias son inversas a las similitudes (menor distancia = mayor probabilidad),
    utilizamos el score de similitud s = -d para los cálculos de scikit-learn.
    """
    if len(np.unique(labels)) < 2:
        logger.warning("Menos de 2 clases presentes en las etiquetas; no se puede calcular ROC/EER.")
        return {
            "roc_auc": 0.0,
            "eer": 0.0,
            "eer_pct": 0.0,
            "eer_threshold": 0.0
        }

    scores = -distances
    fpr, tpr, roc_thresholds = roc_curve(labels, scores)
    roc_auc = float(auc(fpr, tpr))

    # FNR = 1 - TPR = FNMR
    fnr = 1.0 - tpr
    diffs = np.abs(fpr - fnr)

    if len(diffs) == 0 or np.all(np.isnan(diffs)):
        return {
            "roc_auc": roc_auc,
            "eer": 0.0,
            "eer_pct": 0.0,
            "eer_threshold": 0.0
        }

    # EER: punto donde FMR (FPR) ≈ FNMR (FNR)
    eer_idx = int(np.nanargmin(diffs))
    eer_value = float((fpr[eer_idx] + fnr[eer_idx]) / 2.0)
    eer_threshold_distance = float(-roc_thresholds[eer_idx])

    return {
        "roc_auc": roc_auc,
        "eer": eer_value,
        "eer_pct": float(eer_value * 100.0),
        "eer_threshold": eer_threshold_distance
    }


# =========================================================================
#            PRUEBA DE ESTRÉS 1:N EN CHROMADB (EN MEMORIA)
# =========================================================================

def run_chroma_1n_stress_test(
    num_identities: int = 1000,
    num_queries: int = 50,
    embedding_dim: int = 512,
    seed_embeddings: list[list[float]] = None
) -> dict:
    """
    Ejecuta una prueba de estrés 1:N sobre una instancia efímera de ChromaDB en memoria,
    utilizando la misma configuración de grafo HNSW con métrica coseno de app.services.storage.
    
    Mide:
    - Tiempo de enrolamiento masivo de identidades.
    - Latencia media, mediana, P95, P99, mínima y máxima de consultas 1:N.
    """
    logger.info("🧪 Configurando instancia efímera en memoria de ChromaDB (HNSW Cosine)...")
    client = chromadb.EphemeralClient()
    collection_name = f"lfw_benchmark_hnsw_{int(time.time())}"
    
    # Misma configuración métrica de app/services/storage.py
    collection = client.create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"}
    )

    logger.info(f"📥 Generando y enrolando {num_identities} identidades en ChromaDB...")
    np.random.seed(42)

    # Reutilizar embeddings reales si están disponibles o generar sintéticos normalizados L2
    enrolled_embeddings = []
    if seed_embeddings and len(seed_embeddings) > 0:
        for emb in seed_embeddings[:num_identities]:
            enrolled_embeddings.append(l2_normalize(emb).tolist())

    remaining = num_identities - len(enrolled_embeddings)
    if remaining > 0:
        synth_matrix = np.random.randn(remaining, embedding_dim).astype(np.float32)
        norms = np.linalg.norm(synth_matrix, axis=1, keepdims=True)
        synth_normalized = (synth_matrix / np.maximum(norms, 1e-12)).tolist()
        enrolled_embeddings.extend(synth_normalized)

    ids = [f"USER_BENCH_{i:04d}" for i in range(num_identities)]
    metadatas = [
        {"name": f"User Benchmark {i}", "role": "Employee", "enrolled_at": datetime.utcnow().isoformat()}
        for i in range(num_identities)
    ]

    t0_enroll = time.perf_counter()
    # Enrolamiento en lotes para optimizar rendimiento de ingestión
    batch_size = 250
    for i in range(0, num_identities, batch_size):
        collection.add(
            ids=ids[i:i + batch_size],
            embeddings=enrolled_embeddings[i:i + batch_size],
            metadatas=metadatas[i:i + batch_size]
        )
    enroll_time_total_ms = (time.perf_counter() - t0_enroll) * 1000.0

    logger.info(f"✅ {num_identities} identidades enroladas en {enroll_time_total_ms:.2f}ms")

    # Selección de sondas de consulta (queries)
    logger.info(f"⏱️ Ejecutando {num_queries} consultas 1:N de búsqueda por similitud más cercana...")
    query_indices = np.random.choice(num_identities, size=num_queries, replace=False)
    query_vectors = []
    for idx in query_indices:
        # Añadir un ligero ruido Gaussiano simulando varianza biométrica real
        base_v = np.array(enrolled_embeddings[idx], dtype=np.float32)
        noise = np.random.normal(0, 0.02, embedding_dim).astype(np.float32)
        probe = l2_normalize(base_v + noise).tolist()
        query_vectors.append(probe)

    latencies_ms = []
    # Ejecutar 5 consultas previas de 'calentamiento' (warmup) del índice HNSW
    for w_i in range(min(5, len(query_vectors))):
        _ = collection.query(query_embeddings=[query_vectors[w_i]], n_results=1)

    # Medición estricta
    for q_vec in query_vectors:
        t_start = time.perf_counter()
        results = collection.query(query_embeddings=[q_vec], n_results=1)
        t_elapsed = (time.perf_counter() - t_start) * 1000.0
        latencies_ms.append(t_elapsed)

    latencies_arr = np.array(latencies_ms)
    mean_lat = float(np.mean(latencies_arr))
    median_lat = float(np.median(latencies_arr))
    p95_lat = float(np.percentile(latencies_arr, 95))
    p99_lat = float(np.percentile(latencies_arr, 99))
    min_lat = float(np.min(latencies_arr))
    max_lat = float(np.max(latencies_arr))

    return {
        "enrolled_identities": num_identities,
        "embedding_dimensions": embedding_dim,
        "index_metric": "cosine",
        "total_enroll_time_ms": round(enroll_time_total_ms, 2),
        "query_benchmark": {
            "num_queries_executed": num_queries,
            "mean_latency_ms": round(mean_lat, 3),
            "median_latency_ms": round(median_lat, 3),
            "p95_latency_ms": round(p95_lat, 3),
            "p99_latency_ms": round(p99_lat, 3),
            "min_latency_ms": round(min_lat, 3),
            "max_latency_ms": round(max_lat, 3)
        }
    }


# =========================================================================
#                    EJECUCIÓN DEL BENCHMARK
# =========================================================================

def run_lfw_benchmark(max_pairs: int = None, skip_chroma: bool = False, output_file: str = None) -> dict:
    """
    Función principal de ejecución del benchmark LFW.
    """
    logger.info("=================================================================")
    logger.info("   FACESENTINEL — BENCHMARK DE VALIDACIÓN BIOMÉTRICA (LFW)")
    logger.info("   Estándar: ISO/IEC 19795-1 | Modelo: ArcFace (512 dimensiones)")
    logger.info("=================================================================")

    # 1. Cargar pares de prueba de LFW (versión estándar scikit-learn 'test', color=True)
    logger.info("📦 Cargando conjunto de prueba LFW ('test', color=True)...")
    t0_data = time.perf_counter()
    lfw_test = fetch_lfw_pairs(subset="test", color=True)
    load_time_s = time.perf_counter() - t0_data
    total_available_pairs = len(lfw_test.pairs)
    logger.info(f"✅ Dataset cargado en {load_time_s:.2f}s. Pares disponibles: {total_available_pairs}")

    pairs_to_process = total_available_pairs
    if max_pairs and max_pairs > 0 and max_pairs < total_available_pairs:
        pairs_to_process = max_pairs
        logger.info(f"⚡ Modo acotado activado: seleccionando muestra balanceada de {pairs_to_process} pares.")
        # Muestra balanceada de pares genuinos (label 1) e impostores (label 0)
        gen_idx = np.where(lfw_test.target == 1)[0]
        imp_idx = np.where(lfw_test.target == 0)[0]
        n_gen = pairs_to_process // 2
        n_imp = pairs_to_process - n_gen
        selected_idx = np.concatenate([gen_idx[:n_gen], imp_idx[:n_imp]])
        pairs_data = lfw_test.pairs[selected_idx]
        target_labels = lfw_test.target[selected_idx]
    else:
        pairs_data = lfw_test.pairs
        target_labels = lfw_test.target

    # 2. Extracción de embeddings mediante el pipeline de producción FaceSentinel
    valid_distances = []
    valid_labels = []
    extraction_times_ms = []
    valid_embeddings_pool = []

    failed_detection_count = 0
    t0_extract = time.perf_counter()

    logger.info(f"🔍 Extrayendo características biométricas con FaceSentinel ({settings.AI_MODEL_NAME})...")

    embedding_cache = {}

    def get_cached_embedding(img_raw):
        key = hash(img_raw.tobytes())
        if key in embedding_cache:
            return embedding_cache[key]
        img_bgr = preprocess_lfw_image(img_raw)
        emb, t_ms = get_embedding(img_bgr)
        embedding_cache[key] = (emb, t_ms)
        return emb, t_ms

    for i in range(pairs_to_process):
        img1_raw = pairs_data[i][0]
        img2_raw = pairs_data[i][1]
        label = int(target_labels[i])

        # Inferencia con get_embedding() de app.services.face_recognition (con caché en memoria)
        emb1, t1_ms = get_cached_embedding(img1_raw)
        emb2, t2_ms = get_cached_embedding(img2_raw)

        # Si el detector rechaza alguna imagen (sin rostro anatómico verificable)
        if emb1 is None or emb2 is None:
            failed_detection_count += 1
            continue

        extraction_times_ms.extend([t1_ms, t2_ms])
        valid_embeddings_pool.extend([emb1, emb2])

        # Calcular distancia coseno d(u, v) = 1 - (u · v)
        dist = compute_cosine_distance(emb1, emb2)
        valid_distances.append(dist)
        valid_labels.append(label)

        if (i + 1) % 50 == 0 or (i + 1) == pairs_to_process:
            pct = ((i + 1) / pairs_to_process) * 100.0
            avg_t = np.mean(extraction_times_ms) if extraction_times_ms else 0.0
            logger.info(f"  Progreso: {i + 1}/{pairs_to_process} ({pct:.1f}%) | Latencia promedio IA: {avg_t:.1f}ms/rostro")

    total_extract_time_s = time.perf_counter() - t0_extract
    evaluated_pairs_count = len(valid_distances)

    if evaluated_pairs_count == 0:
        logger.error("❌ No se pudo procesar ningún par de rostros exitosamente.")
        return {}

    distances_arr = np.array(valid_distances)
    labels_arr = np.array(valid_labels)

    # 3. Métricas ISO/IEC 19795-1 y comparación de umbrales
    thresh_literature = 0.68
    thresh_calibrated = float(settings.FACE_MATCH_THRESHOLD)  # 0.60

    metrics_lit = calculate_iso_metrics(distances_arr, labels_arr, thresh_literature)
    metrics_cal = calculate_iso_metrics(distances_arr, labels_arr, thresh_calibrated)
    roc_eer_results = compute_roc_and_eer(distances_arr, labels_arr)

    # Tasa de fallo en adquisición (Failure to Acquire - FTA) según ISO 19795-1
    total_samples = pairs_to_process * 2
    failed_samples = failed_detection_count * 2  # cota superior
    fta_rate = failed_samples / total_samples if total_samples > 0 else 0.0

    # 4. Prueba de estrés 1:N en ChromaDB
    chroma_results = {}
    if not skip_chroma:
        chroma_results = run_chroma_1n_stress_test(
            num_identities=1000,
            num_queries=50,
            embedding_dim=len(valid_embeddings_pool[0]) if valid_embeddings_pool else 512,
            seed_embeddings=valid_embeddings_pool[:200]
        )

    # 5. Estructurar reporte completo
    report = {
        "benchmark_metadata": {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "standard": "ISO/IEC 19795-1 (Biometric performance testing and reporting)",
            "dataset": "Labeled Faces in the Wild (LFW)",
            "dataset_subset": "test",
            "total_pairs_requested": pairs_to_process,
            "pairs_successfully_evaluated": evaluated_pairs_count,
            "failed_detection_pairs": failed_detection_count,
            "failure_to_acquire_rate_fta": round(fta_rate, 4),
            "total_evaluation_time_seconds": round(total_extract_time_s, 2),
            "mean_extraction_latency_ms": round(float(np.mean(extraction_times_ms)), 2)
        },
        "pipeline_configuration": {
            "model_name": settings.AI_MODEL_NAME,
            "embedding_dimension": len(valid_embeddings_pool[0]) if valid_embeddings_pool else 512,
            "distance_metric": "cosine",
            "distance_formula": "d(u, v) = 1.0 - (u · v)",
            "detectors_cascade": [
                "OpenCV Haar / DNN Cascade with forced alignment",
                "MediaPipe FaceMesh 3D (Sub-pixel landmark fallback)"
            ]
        },
        "iso_metrics": {
            "literature_threshold": metrics_lit,
            "calibrated_threshold": metrics_cal,
            "roc_auc": round(roc_eer_results["roc_auc"], 4),
            "eer": round(roc_eer_results["eer"], 4),
            "eer_pct": round(roc_eer_results["eer_pct"], 2),
            "eer_optimal_threshold": round(roc_eer_results["eer_threshold"], 4)
        },
        "chromadb_1n_stress_test": chroma_results
    }

    # 6. Imprimir informe en consola
    print_formatted_summary(report)

    # 7. Guardar en JSON para la tesis
    if not output_file:
        data_dir = BASE_DIR / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        output_file = str(data_dir / "lfw_benchmark_results.json")

    out_path = Path(output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    logger.info(f"📁 Resultados exportados exitosamente a: {out_path.resolve()}")
    return report


def print_formatted_summary(report: dict):
    """Muestra un resumen formateado de alta calidad en la terminal."""
    meta = report["benchmark_metadata"]
    pipe = report["pipeline_configuration"]
    iso = report["iso_metrics"]
    lit = iso["literature_threshold"]
    cal = iso["calibrated_threshold"]
    chroma = report.get("chromadb_1n_stress_test", {})

    print("\n" + "=" * 80)
    print("                    FACESENTINEL — RESULTADOS LFW BENCHMARK")
    print("                      Estándar Internacional ISO/IEC 19795-1")
    print("=" * 80)
    print(f"  • Modelo IA                : {pipe['model_name']} ({pipe['embedding_dimension']} dimensiones)")
    print(f"  • Métrica de Distancia     : {pipe['distance_metric']} [HNSW Cosine]")
    print(f"  • Pares Evaluados          : {meta['pairs_successfully_evaluated']} / {meta['total_pairs_requested']}")
    print(f"  • Fallo de Adquisición FTA : {meta['failure_to_acquire_rate_fta'] * 100:.2f}%")
    print(f"  • Latencia Extracción Media: {meta['mean_extraction_latency_ms']:.2f} ms / rostro")
    print("-" * 80)
    print("  COMPARATIVA DE UMBRALES DE DECISIÓN:")
    print(f"  {'Métrica':<30} | {'Literatura (d < 0.68)':<20} | {'FaceSentinel (d < 0.60)':<20}")
    print("  " + "-" * 76)
    print(f"  {'Exactitud Global (Accuracy)':<30} | {lit['accuracy_pct']:>18.2f}% | {cal['accuracy_pct']:>18.2f}%")
    print(f"  {'FMR (Falsa Aceptación)':<30} | {lit['fmr_pct']:>18.2f}% | {cal['fmr_pct']:>18.2f}%")
    print(f"  {'FNMR (Falso Rechazo)':<30} | {lit['fnmr_pct']:>18.2f}% | {cal['fnmr_pct']:>18.2f}%")
    print(f"  {'Verdaderos Matches (TM)':<30} | {lit['confusion_matrix']['true_matches']:>19} | {cal['confusion_matrix']['true_matches']:>19}")
    print(f"  {'Falsos Matches (FM)':<30} | {lit['confusion_matrix']['false_matches']:>19} | {cal['confusion_matrix']['false_matches']:>19}")
    print(f"  {'Verdaderos Non-Matches (TNM)':<30} | {lit['confusion_matrix']['true_non_matches']:>19} | {cal['confusion_matrix']['true_non_matches']:>19}")
    print(f"  {'Falsos Non-Matches (FNM)':<30} | {lit['confusion_matrix']['false_non_matches']:>19} | {cal['confusion_matrix']['false_non_matches']:>19}")
    print("-" * 80)
    print("  MÉTRICAS GLOBALES DE DISCRIMINACIÓN BIOMÉTRICA:")
    print(f"  • ROC AUC (Área Bajo la Curva) : {iso['roc_auc']:.4f}")
    print(f"  • EER (Equal Error Rate)       : {iso['eer_pct']:.2f}% (en umbral óptimo d = {iso['eer_optimal_threshold']:.4f})")
    print("-" * 80)

    if chroma and "query_benchmark" in chroma:
        qb = chroma["query_benchmark"]
        print("  PRUEBA DE ESTRÉS 1:N EN CHROMADB (INSTANCIA EFÍMERA EN MEMORIA):")
        print(f"  • Identidades Enroladas        : {chroma['enrolled_identities']:,}")
        print(f"  • Espacio Indexado             : {chroma['index_metric']} (Grafo HNSW)")
        print(f"  • Consultas 1:N Ejecutadas     : {qb['num_queries_executed']}")
        print(f"  • Latencia Media de Búsqueda   : {qb['mean_latency_ms']:.3f} ms")
        print(f"  • Mediana (P50)                : {qb['median_latency_ms']:.3f} ms")
        print(f"  • Percentil 95 (P95)           : {qb['p95_latency_ms']:.3f} ms")
        print(f"  • Percentil 99 (P99)           : {qb['p99_latency_ms']:.3f} ms")
        print(f"  • Rango (Min / Max)            : {qb['min_latency_ms']:.3f} ms / {qb['max_latency_ms']:.3f} ms")
        print("=" * 80 + "\n")


# =========================================================================
#                    PUNTO DE ENTRADA CLI
# =========================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Benchmark biométrico masivo con LFW para FaceSentinel (ISO/IEC 19795-1)"
    )
    parser.add_argument(
        "--max-pairs",
        type=int,
        default=None,
        help="Limita el número de pares a evaluar (útil para pruebas rápidas de validación)."
    )
    parser.add_argument(
        "--skip-chroma",
        action="store_true",
        help="Omite la prueba de estrés 1:N de ChromaDB."
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Ruta donde guardar el reporte JSON (por defecto: data/lfw_benchmark_results.json)."
    )

    args = parser.parse_args()
    run_lfw_benchmark(
        max_pairs=args.max_pairs,
        skip_chroma=args.skip_chroma,
        output_file=args.output
    )


if __name__ == "__main__":
    main()
