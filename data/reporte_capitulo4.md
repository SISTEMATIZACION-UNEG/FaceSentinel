# FaceSentinel — Resultados Experimentales y Evaluación Científica del Capítulo IV

**Fecha de Evaluación:** 2026-10-05 19:38:42  
**Dataset Analizado:** `metricas_tesis.csv`  
**Total de Ensayos Registrados:** 18 intentos de autenticación

---

## 1. Matriz de Confusión Global de Control de Acceso

La siguiente matriz clasifica las decisiones del sistema entre accesos legítimos autorizados frente a intentos indebidos (ataques de presentación con foto/video e impostores no registrados):

| Condición Real \ Decisión Sistema | Acceso Concedido (GRANTED) | Acceso Denegado (DENIED) | Total Real |
|:---|:---:|:---:|:---:|
| **Sujeto Autorizado (Bona Fide Live)** | **Verdaderos Positivos (VP): 11** | **Falsos Negativos (FN): 5** | 16 |
| **Intento Indebido (Ataques + Impostores)** | **Falsos Positivos (FP): 0** | **Verdaderos Negativos (VN): 2** | 2 |
| **Total Clasificado** | 11 | 7 | **18** |

### Indicadores Globales de Seguridad
- **Exactitud General (Accuracy):** `72.22%`
- **Precisión (Precision):** `100.00%`
- **Sensibilidad / Tasa de Acierto (Recall / TPR):** `68.75%`
- **Especificidad (TNR):** `100.00%`
- **F1-Score:** `81.48%`
- **Tasa Global de Falsa Aceptación (FAR):** `0.00%` *(Vulnerabilidad de acceso)*
- **Tasa Global de Falso Rechazo (FRR):** `31.25%` *(Fricción de usuario)*

---

## 2. Evaluación Específica de Detección de Ataques de Presentación (PAD / ISO/IEC 30107-3)

Evaluación del subsistema Anti-Spoofing en el borde y servidor (MediaPipe Blink EAR + Textura LBP):

| Indicador PAD (ISO/IEC 30107-3) | Valor Obtenido | Muestras Evaluadas | Interpretación Técnica |
|:---|:---:|:---:|:---|
| **APCER - Fotos Impresas/Pantalla** | `0.00%` | 2 intentos | Fotos que burlaron la detección de liveness |
| **APCER - Video Replay con Parpadeo** | `0.00%` | 0 intentos | Videos en smartphone que lograron traspasar |
| **APCER Global (Ataques no detectados)** | **`0.00%`** | 2 ataques | Tasa total de filtración de ataques de presentación |
| **BPCER (Falso rechazo a vivos genuinos)**| **`6.25%`** | 16 intentos | Usuarios vivos confundidos erróneamente con spoofing |
| **ACER (Error Medio de Clasificación)**   | **`3.12%`** | 18 muestras | Media balanceada entre APCER y BPCER |

---

## 3. Evaluación del Reconocimiento Facial Biométrico (ISO/IEC 19795-1)

Rendimiento del modelo DeepFace ArcFace (512 dimensiones) con indexación vectorial ChromaDB (HNSW):

| Métrica Biometría Facial | Valor Obtenido | Muestras | Interpretación |
|:---|:---:|:---:|:---|
| **FNMR (False Non-Match Rate)** | `25.00%` | 16 | Usuarios autorizados vivos rechazados por distancia $d > 0.75$ |
| **FMR (False Match Rate)** | `0.00%` | 0 | Impostores vivos aceptados con distancia $d \le 0.75$ |
| **Distancia Coseno (Genuine Match)** | `0.05 ± 0.08` | 11 | Distancia promedio para accesos autorizados |
| **Distancia Coseno (Impostores/Desconocidos)** | `0.86 ± 0.04` | 4 | Distancia promedio para rostros no emparejados |

---

## 4. Análisis de Robustez ante Condiciones Ambientales (Iluminación)

| Entorno Evaluado | Muestras Totales | Decisiones Correctas | Fallos | Exactitud (%) | Latencia Media E2E (ms) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Iluminación Normal (Oficina/Lab)** | 16 | 11 | 5 | 68.75% | 479.74 ms |
| **Baja Iluminación (< 50 lux)** | 0 | 0 | 0 | 0.00% | 0.0 ms |
| **Alta Luz / Contraluz (> 1000 lux)** | 2 | 2 | 0 | 100.00% | 71.0 ms |

---

## 5. Benchmarking de Latencias del Pipeline (Milisegundos)

| Componente de Arquitectura | Media (ms) | Desv. Est. (ms) | Percentil 95 (ms) | Mín (ms) | Máx (ms) | Muestras |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Borde: MediaPipe Face Mesh (EAR)** | `8.32` | `±7.19` | `22.5` | `4.18` | `22.5` | 18 |
| **Borde: Procesamiento Total Borde** | `13.15` | `±12.5` | `38.0` | `6.18` | `38.0` | 18 |
| **Red Troncal: Tránsito RTT** | `14.6` | `±0.6` | `15.2` | `14.0` | `15.2` | 4 |
| **Servidor: LBP Entropía Textura** | `12.7` | `±1.06` | `15.62` | `11.0` | `15.62` | 18 |
| **Servidor: FFT Espectro Frecuencia** | `7.8` | `±0.3` | `8.1` | `7.5` | `8.1` | 4 |
| **Servidor: ArcFace Extracción 512d** | `266.76` | `±12.55` | `287.93` | `245.0` | `287.93` | 15 |
| **Servidor: ChromaDB Búsqueda Vectorial** | `3.02` | `±3.22` | `11.2` | `1.35` | `11.2` | 15 |
| **Servidor: SQLite Validación ACL/RBAC** | `163.97` | `±86.63` | `217.18` | `1.8` | `217.18` | 18 |
| **Servidor: Latencia Total Backend** | `417.93` | `±167.3` | `530.68` | `22.0` | `530.68` | 18 |
| **Latencia Total End-to-End** | **`434.32`** | **`±152.33`** | **`537.13`** | **`71.0`** | **`537.13`** | 18 |

---

## 6. Eficiencia de Auditoría Blockchain (Smart Contract en Ethereum)

- **Consumo de Gas Promedio (`logAuthentication`):** `195,557 gas` (Mín: `68,432` | Máx: `247,659`)
- **Tiempo de Sellado de Bloque (Sealing Time):** `54.71 ms` (`±31.1 ms` | P95: `115.4 ms`)
- **Total de Transacciones Notariadas en Cadena:** `18` eventos
