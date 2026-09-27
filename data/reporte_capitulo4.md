# FaceSentinel — Resultados Experimentales y Evaluación Científica del Capítulo IV

**Fecha de Evaluación:** 2026-09-26 19:06:04  
**Dataset Analizado:** `metricas_tesis.csv`  
**Total de Ensayos Registrados:** 81 intentos de autenticación

---

## 1. Matriz de Confusión Global de Control de Acceso

La siguiente matriz clasifica las decisiones del sistema entre accesos legítimos autorizados frente a intentos indebidos (ataques de presentación con foto/video e impostores no registrados):

| Condición Real \ Decisión Sistema | Acceso Concedido (GRANTED) | Acceso Denegado (DENIED) | Total Real |
|:---|:---:|:---:|:---:|
| **Sujeto Autorizado (Bona Fide Live)** | **Verdaderos Positivos (VP): 22** | **Falsos Negativos (FN): 7** | 29 |
| **Intento Indebido (Ataques + Impostores)** | **Falsos Positivos (FP): 4** | **Verdaderos Negativos (VN): 48** | 52 |
| **Total Clasificado** | 26 | 55 | **81** |

### Indicadores Globales de Seguridad
- **Exactitud General (Accuracy):** `86.42%`
- **Precisión (Precision):** `84.62%`
- **Sensibilidad / Tasa de Acierto (Recall / TPR):** `75.86%`
- **Especificidad (TNR):** `92.31%`
- **F1-Score:** `80.00%`
- **Tasa Global de Falsa Aceptación (FAR):** `7.69%` *(Vulnerabilidad de acceso)*
- **Tasa Global de Falso Rechazo (FRR):** `24.14%` *(Fricción de usuario)*

---

## 2. Evaluación Específica de Detección de Ataques de Presentación (PAD / ISO/IEC 30107-3)

Evaluación del subsistema Anti-Spoofing en el borde y servidor (MediaPipe Blink EAR + Textura LBP):

| Indicador PAD (ISO/IEC 30107-3) | Valor Obtenido | Muestras Evaluadas | Interpretación Técnica |
|:---|:---:|:---:|:---|
| **APCER - Fotos Impresas/Pantalla** | `0.00%` | 21 intentos | Fotos que burlaron la detección de liveness |
| **APCER - Video Replay con Parpadeo** | `35.48%` | 31 intentos | Videos en smartphone que lograron traspasar |
| **APCER Global (Ataques no detectados)** | **`21.15%`** | 52 ataques | Tasa total de filtración de ataques de presentación |
| **BPCER (Falso rechazo a vivos genuinos)**| **`6.90%`** | 29 intentos | Usuarios vivos confundidos erróneamente con spoofing |
| **ACER (Error Medio de Clasificación)**   | **`14.03%`** | 81 muestras | Media balanceada entre APCER y BPCER |

---

## 3. Evaluación del Reconocimiento Facial Biométrico (ISO/IEC 19795-1)

Rendimiento del modelo DeepFace ArcFace (512 dimensiones) con indexación vectorial ChromaDB (HNSW):

| Métrica Biometría Facial | Valor Obtenido | Muestras | Interpretación |
|:---|:---:|:---:|:---|
| **FNMR (False Non-Match Rate)** | `17.24%` | 29 | Usuarios autorizados vivos rechazados por distancia $d > 0.75$ |
| **FMR (False Match Rate)** | `0.00%` | 0 | Impostores vivos aceptados con distancia $d \le 0.75$ |
| **Distancia Coseno (Genuine Match)** | `0.39 ± 0.15` | 26 | Distancia promedio para accesos autorizados |
| **Distancia Coseno (Impostores/Desconocidos)** | `0.84 ± 0.1` | 12 | Distancia promedio para rostros no emparejados |

---

## 4. Análisis de Robustez ante Condiciones Ambientales (Iluminación)

| Entorno Evaluado | Muestras Totales | Decisiones Correctas | Fallos | Exactitud (%) | Latencia Media E2E (ms) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Iluminación Normal (Oficina/Lab)** | 81 | 70 | 11 | 86.42% | 357.39 ms |
| **Baja Iluminación (< 50 lux)** | 0 | 0 | 0 | 0.00% | 0.0 ms |
| **Alta Luz / Contraluz (> 1000 lux)** | 0 | 0 | 0 | 0.00% | 0.0 ms |

---

## 5. Benchmarking de Latencias del Pipeline (Milisegundos)

| Componente de Arquitectura | Media (ms) | Desv. Est. (ms) | Percentil 95 (ms) | Mín (ms) | Máx (ms) | Muestras |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Borde: MediaPipe Face Mesh (EAR)** | `4.27` | `±1.07` | `5.73` | `2.5` | `6.61` | 81 |
| **Borde: Procesamiento Total Borde** | `6.27` | `±1.07` | `7.73` | `4.5` | `8.61` | 81 |
| **Red Troncal: Tránsito RTT** | `0.0` | `±0.0` | `0.0` | `0.0` | `0.0` | 0 |
| **Servidor: LBP Entropía Textura** | `12.18` | `±1.08` | `14.39` | `10.92` | `17.36` | 81 |
| **Servidor: FFT Espectro Frecuencia** | `0.79` | `±0.25` | `1.38` | `0.6` | `1.95` | 81 |
| **Servidor: ArcFace Extracción 512d** | `241.55` | `±20.13` | `293.28` | `212.12` | `294.86` | 38 |
| **Servidor: ChromaDB Búsqueda Vectorial** | `1.75` | `±0.56` | `2.79` | `1.27` | `4.64` | 38 |
| **Servidor: SQLite Validación ACL/RBAC** | `209.65` | `±1.49` | `212.74` | `207.88` | `215.53` | 81 |
| **Servidor: Latencia Total Backend** | `351.12` | `±124.08` | `497.99` | `230.41` | `545.94` | 81 |
| **Latencia Total End-to-End** | **`357.39`** | **`±124.43`** | **`504.54`** | **`234.91`** | **`552.25`** | 81 |

---

## 6. Eficiencia de Auditoría Blockchain (Smart Contract en Ethereum)

- **Consumo de Gas Promedio (`logAuthentication`):** `209,587 gas` (Mín: `187,347` | Máx: `247,443`)
- **Tiempo de Sellado de Bloque (Sealing Time):** `33.74 ms` (`±2.57 ms` | P95: `36.88 ms`)
- **Total de Transacciones Notariadas en Cadena:** `81` eventos
