# FaceSentinel — Resultados Experimentales y Evaluación Científica del Capítulo IV

**Fecha de Evaluación:** 2026-09-27 12:06:15  
**Dataset Analizado:** `metricas_tesis.csv`  
**Total de Ensayos Registrados:** 454 intentos de autenticación

---

## 1. Matriz de Confusión Global de Control de Acceso

La siguiente matriz clasifica las decisiones del sistema entre accesos legítimos autorizados frente a intentos indebidos (ataques de presentación con foto/video e impostores no registrados):

| Condición Real \ Decisión Sistema | Acceso Concedido (GRANTED) | Acceso Denegado (DENIED) | Total Real |
|:---|:---:|:---:|:---:|
| **Sujeto Autorizado (Bona Fide Live)** | **Verdaderos Positivos (VP): 103** | **Falsos Negativos (FN): 11** | 114 |
| **Intento Indebido (Ataques + Impostores)** | **Falsos Positivos (FP): 132** | **Verdaderos Negativos (VN): 208** | 340 |
| **Total Clasificado** | 235 | 219 | **454** |

### Indicadores Globales de Seguridad
- **Exactitud General (Accuracy):** `68.50%`
- **Precisión (Precision):** `43.83%`
- **Sensibilidad / Tasa de Acierto (Recall / TPR):** `90.35%`
- **Especificidad (TNR):** `61.18%`
- **F1-Score:** `59.03%`
- **Tasa Global de Falsa Aceptación (FAR):** `38.82%` *(Vulnerabilidad de acceso)*
- **Tasa Global de Falso Rechazo (FRR):** `9.65%` *(Fricción de usuario)*

---

## 2. Evaluación Específica de Detección de Ataques de Presentación (PAD / ISO/IEC 30107-3)

Evaluación del subsistema Anti-Spoofing en el borde y servidor (MediaPipe Blink EAR + Textura LBP):

| Indicador PAD (ISO/IEC 30107-3) | Valor Obtenido | Muestras Evaluadas | Interpretación Técnica |
|:---|:---:|:---:|:---|
| **APCER - Fotos Impresas/Pantalla** | `99.16%` | 119 intentos | Fotos que burlaron la detección de liveness |
| **APCER - Video Replay con Parpadeo** | `8.41%` | 107 intentos | Videos en smartphone que lograron traspasar |
| **APCER Global (Ataques no detectados)** | **`56.19%`** | 226 ataques | Tasa total de filtración de ataques de presentación |
| **BPCER (Falso rechazo a vivos genuinos)**| **`1.75%`** | 114 intentos | Usuarios vivos confundidos erróneamente con spoofing |
| **ACER (Error Medio de Clasificación)**   | **`28.97%`** | 340 muestras | Media balanceada entre APCER y BPCER |

---

## 3. Evaluación del Reconocimiento Facial Biométrico (ISO/IEC 19795-1)

Rendimiento del modelo DeepFace ArcFace (512 dimensiones) con indexación vectorial ChromaDB (HNSW):

| Métrica Biometría Facial | Valor Obtenido | Muestras | Interpretación |
|:---|:---:|:---:|:---|
| **FNMR (False Non-Match Rate)** | `7.89%` | 114 | Usuarios autorizados vivos rechazados por distancia $d > 0.75$ |
| **FMR (False Match Rate)** | `8.77%` | 114 | Impostores vivos aceptados con distancia $d \le 0.75$ |
| **Distancia Coseno (Genuine Match)** | `0.37 ± 0.11` | 235 | Distancia promedio para accesos autorizados |
| **Distancia Coseno (Impostores/Desconocidos)** | `0.78 ± 0.07` | 117 | Distancia promedio para rostros no emparejados |

---

## 4. Análisis de Robustez ante Condiciones Ambientales (Iluminación)

| Entorno Evaluado | Muestras Totales | Decisiones Correctas | Fallos | Exactitud (%) | Latencia Media E2E (ms) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Iluminación Normal (Oficina/Lab)** | 454 | 311 | 143 | 68.50% | 439.48 ms |
| **Baja Iluminación (< 50 lux)** | 0 | 0 | 0 | 0.00% | 0.0 ms |
| **Alta Luz / Contraluz (> 1000 lux)** | 0 | 0 | 0 | 0.00% | 0.0 ms |

---

## 5. Benchmarking de Latencias del Pipeline (Milisegundos)

| Componente de Arquitectura | Media (ms) | Desv. Est. (ms) | Percentil 95 (ms) | Mín (ms) | Máx (ms) | Muestras |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Borde: MediaPipe Face Mesh (EAR)** | `4.13` | `±1.02` | `5.39` | `2.5` | `7.81` | 454 |
| **Borde: Procesamiento Total Borde** | `6.13` | `±1.02` | `7.39` | `4.5` | `9.81` | 454 |
| **Red Troncal: Tránsito RTT** | `0.0` | `±0.0` | `0.0` | `0.0` | `0.0` | 0 |
| **Servidor: LBP Entropía Textura** | `12.36` | `±1.44` | `14.98` | `10.66` | `25.3` | 454 |
| **Servidor: FFT Espectro Frecuencia** | `0.79` | `±0.36` | `1.27` | `0.57` | `4.8` | 454 |
| **Servidor: ArcFace Extracción 512d** | `249.5` | `±81.6` | `295.0` | `192.62` | `1399.74` | 352 |
| **Servidor: ChromaDB Búsqueda Vectorial** | `1.64` | `±0.42` | `2.12` | `1.12` | `5.81` | 352 |
| **Servidor: SQLite Validación ACL/RBAC** | `211.1` | `±6.58` | `220.64` | `207.55` | `276.17` | 454 |
| **Servidor: Latencia Total Backend** | `433.35` | `±130.35` | `538.4` | `229.22` | `1633.4` | 454 |
| **Latencia Total End-to-End** | **`439.48`** | **`±130.14`** | **`545.02`** | **`235.55`** | **`1640.14`** | 454 |

---

## 6. Eficiencia de Auditoría Blockchain (Smart Contract en Ethereum)

- **Consumo de Gas Promedio (`logAuthentication`):** `224,080 gas` (Mín: `187,347` | Máx: `252,417`)
- **Tiempo de Sellado de Bloque (Sealing Time):** `35.18 ms` (`±4.34 ms` | P95: `41.51 ms`)
- **Total de Transacciones Notariadas en Cadena:** `454` eventos
