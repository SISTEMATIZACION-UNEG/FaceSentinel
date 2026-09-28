# FaceSentinel — Resultados Experimentales y Evaluación Científica del Capítulo IV

**Fecha de Evaluación:** 2026-09-27 18:47:23  
**Dataset Analizado:** `metricas_tesis.csv`  
**Total de Ensayos Registrados:** 421 intentos de autenticación

---

## 1. Matriz de Confusión Global de Control de Acceso

La siguiente matriz clasifica las decisiones del sistema entre accesos legítimos autorizados frente a intentos indebidos (ataques de presentación con foto/video e impostores no registrados):

| Condición Real \ Decisión Sistema | Acceso Concedido (GRANTED) | Acceso Denegado (DENIED) | Total Real |
|:---|:---:|:---:|:---:|
| **Sujeto Autorizado (Bona Fide Live)** | **Verdaderos Positivos (VP): 88** | **Falsos Negativos (FN): 16** | 104 |
| **Intento Indebido (Ataques + Impostores)** | **Falsos Positivos (FP): 2** | **Verdaderos Negativos (VN): 315** | 317 |
| **Total Clasificado** | 90 | 331 | **421** |

### Indicadores Globales de Seguridad
- **Exactitud General (Accuracy):** `95.72%`
- **Precisión (Precision):** `97.78%`
- **Sensibilidad / Tasa de Acierto (Recall / TPR):** `84.62%`
- **Especificidad (TNR):** `99.37%`
- **F1-Score:** `90.72%`
- **Tasa Global de Falsa Aceptación (FAR):** `0.63%` *(Vulnerabilidad de acceso)*
- **Tasa Global de Falso Rechazo (FRR):** `15.38%` *(Fricción de usuario)*

---

## 2. Evaluación Específica de Detección de Ataques de Presentación (PAD / ISO/IEC 30107-3)

Evaluación del subsistema Anti-Spoofing en el borde y servidor (MediaPipe Blink EAR + Textura LBP):

| Indicador PAD (ISO/IEC 30107-3) | Valor Obtenido | Muestras Evaluadas | Interpretación Técnica |
|:---|:---:|:---:|:---|
| **APCER - Fotos Impresas/Pantalla** | `1.87%` | 107 intentos | Fotos que burlaron la detección de liveness |
| **APCER - Video Replay con Parpadeo** | `0.00%` | 97 intentos | Videos en smartphone que lograron traspasar |
| **APCER Global (Ataques no detectados)** | **`0.98%`** | 204 ataques | Tasa total de filtración de ataques de presentación |
| **BPCER (Falso rechazo a vivos genuinos)**| **`12.50%`** | 104 intentos | Usuarios vivos confundidos erróneamente con spoofing |
| **ACER (Error Medio de Clasificación)**   | **`6.74%`** | 308 muestras | Media balanceada entre APCER y BPCER |

---

## 3. Evaluación del Reconocimiento Facial Biométrico (ISO/IEC 19795-1)

Rendimiento del modelo DeepFace ArcFace (512 dimensiones) con indexación vectorial ChromaDB (HNSW):

| Métrica Biometría Facial | Valor Obtenido | Muestras | Interpretación |
|:---|:---:|:---:|:---|
| **FNMR (False Non-Match Rate)** | `2.88%` | 104 | Usuarios autorizados vivos rechazados por distancia $d > 0.75$ |
| **FMR (False Match Rate)** | `0.00%` | 113 | Impostores vivos aceptados con distancia $d \le 0.75$ |
| **Distancia Coseno (Genuine Match)** | `0.27 ± 0.05` | 90 | Distancia promedio para accesos autorizados |
| **Distancia Coseno (Impostores/Desconocidos)** | `0.79 ± 0.07` | 113 | Distancia promedio para rostros no emparejados |

---

## 4. Análisis de Robustez ante Condiciones Ambientales (Iluminación)

| Entorno Evaluado | Muestras Totales | Decisiones Correctas | Fallos | Exactitud (%) | Latencia Media E2E (ms) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Iluminación Normal (Oficina/Lab)** | 421 | 403 | 18 | 95.72% | 367.16 ms |
| **Baja Iluminación (< 50 lux)** | 0 | 0 | 0 | 0.00% | 0.0 ms |
| **Alta Luz / Contraluz (> 1000 lux)** | 0 | 0 | 0 | 0.00% | 0.0 ms |

---

## 5. Benchmarking de Latencias del Pipeline (Milisegundos)

| Componente de Arquitectura | Media (ms) | Desv. Est. (ms) | Percentil 95 (ms) | Mín (ms) | Máx (ms) | Muestras |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Borde: MediaPipe Face Mesh (EAR)** | `4.3` | `±1.19` | `5.97` | `2.5` | `10.84` | 421 |
| **Borde: Procesamiento Total Borde** | `6.3` | `±1.19` | `7.97` | `4.5` | `12.84` | 421 |
| **Red Troncal: Tránsito RTT** | `0.0` | `±0.0` | `0.0` | `0.0` | `0.0` | 0 |
| **Servidor: LBP Entropía Textura** | `12.49` | `±1.23` | `14.69` | `10.54` | `21.26` | 421 |
| **Servidor: FFT Espectro Frecuencia** | `0.9` | `±0.32` | `1.58` | `0.6` | `2.74` | 421 |
| **Servidor: ArcFace Extracción 512d** | `250.39` | `±66.47` | `285.55` | `209.15` | `1149.63` | 203 |
| **Servidor: ChromaDB Búsqueda Vectorial** | `1.59` | `±0.26` | `2.06` | `1.1` | `2.39` | 203 |
| **Servidor: SQLite Validación ACL/RBAC** | `211.6` | `±2.25` | `214.89` | `208.4` | `230.17` | 421 |
| **Servidor: Latencia Total Backend** | `360.85` | `±134.98` | `513.42` | `232.03` | `1386.93` | 421 |
| **Latencia Total End-to-End** | **`367.16`** | **`±135.4`** | **`520.02`** | **`237.75`** | **`1393.2`** | 421 |

---

## 6. Eficiencia de Auditoría Blockchain (Smart Contract en Ethereum)

- **Consumo de Gas Promedio (`logAuthentication`):** `207,539 gas` (Mín: `187,419` | Máx: `252,489`)
- **Tiempo de Sellado de Bloque (Sealing Time):** `37.72 ms` (`±7.88 ms` | P95: `45.07 ms`)
- **Total de Transacciones Notariadas en Cadena:** `421` eventos
