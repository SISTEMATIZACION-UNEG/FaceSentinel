# FaceSentinel — Resultados Experimentales y Evaluación Científica del Capítulo IV

**Fecha de Evaluación:** 2026-10-05 19:51:10  
**Dataset Analizado:** `metricas_tesis.csv`  
**Total de Ensayos Registrados:** 20 intentos de autenticación

---

## 1. Matriz de Confusión Global de Control de Acceso

La siguiente matriz clasifica las decisiones del sistema entre accesos legítimos autorizados frente a intentos indebidos (ataques de presentación con foto/video e impostores no registrados):

| Condición Real \ Decisión Sistema | Acceso Concedido (GRANTED) | Acceso Denegado (DENIED) | Total Real |
|:---|:---:|:---:|:---:|
| **Sujeto Autorizado (Bona Fide Live)** | **Verdaderos Positivos (VP): 12** | **Falsos Negativos (FN): 5** | 17 |
| **Intento Indebido (Ataques + Impostores)** | **Falsos Positivos (FP): 0** | **Verdaderos Negativos (VN): 3** | 3 |
| **Total Clasificado** | 12 | 8 | **20** |

### Indicadores Globales de Seguridad
- **Exactitud General (Accuracy):** `75.00%`
- **Precisión (Precision):** `100.00%`
- **Sensibilidad / Tasa de Acierto (Recall / TPR):** `70.59%`
- **Especificidad (TNR):** `100.00%`
- **F1-Score:** `82.76%`
- **Tasa Global de Falsa Aceptación (FAR):** `0.00%` *(Vulnerabilidad de acceso)*
- **Tasa Global de Falso Rechazo (FRR):** `29.41%` *(Fricción de usuario)*

---

## 2. Evaluación Específica de Detección de Ataques de Presentación (PAD / ISO/IEC 30107-3)

Evaluación del subsistema Anti-Spoofing en el borde y servidor (MediaPipe Blink EAR + Textura LBP):

| Indicador PAD (ISO/IEC 30107-3) | Valor Obtenido | Muestras Evaluadas | Interpretación Técnica |
|:---|:---:|:---:|:---|
| **APCER - Fotos Impresas/Pantalla** | `0.00%` | 3 intentos | Fotos que burlaron la detección de liveness |
| **APCER - Video Replay con Parpadeo** | `0.00%` | 0 intentos | Videos en smartphone que lograron traspasar |
| **APCER Global (Ataques no detectados)** | **`0.00%`** | 3 ataques | Tasa total de filtración de ataques de presentación |
| **BPCER (Falso rechazo a vivos genuinos)**| **`5.88%`** | 17 intentos | Usuarios vivos confundidos erróneamente con spoofing |
| **ACER (Error Medio de Clasificación)**   | **`2.94%`** | 20 muestras | Media balanceada entre APCER y BPCER |

---

## 3. Evaluación del Reconocimiento Facial Biométrico (ISO/IEC 19795-1)

Rendimiento del modelo DeepFace ArcFace (512 dimensiones) con indexación vectorial ChromaDB (HNSW):

| Métrica Biometría Facial | Valor Obtenido | Muestras | Interpretación |
|:---|:---:|:---:|:---|
| **FNMR (False Non-Match Rate)** | `23.53%` | 17 | Usuarios autorizados vivos rechazados por distancia $d > 0.75$ |
| **FMR (False Match Rate)** | `0.00%` | 0 | Impostores vivos aceptados con distancia $d \le 0.75$ |
| **Distancia Coseno (Genuine Match)** | `0.07 ± 0.1` | 12 | Distancia promedio para accesos autorizados |
| **Distancia Coseno (Impostores/Desconocidos)** | `0.86 ± 0.04` | 4 | Distancia promedio para rostros no emparejados |

---

## 4. Análisis de Robustez ante Condiciones Ambientales (Iluminación)

| Entorno Evaluado | Muestras Totales | Decisiones Correctas | Fallos | Exactitud (%) | Latencia Media E2E (ms) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Iluminación Normal (Oficina/Lab)** | 17 | 12 | 5 | 70.59% | 471.41 ms |
| **Baja Iluminación (< 50 lux)** | 0 | 0 | 0 | 0.00% | 0.0 ms |
| **Alta Luz / Contraluz (> 1000 lux)** | 3 | 3 | 0 | 100.00% | 71.0 ms |

---

## 5. Benchmarking de Latencias del Pipeline (Milisegundos)

| Componente de Arquitectura | Media (ms) | Desv. Est. (ms) | Percentil 95 (ms) | Mín (ms) | Máx (ms) | Muestras |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Borde: MediaPipe Face Mesh (EAR)** | `9.66` | `±7.92` | `22.5` | `4.18` | `22.5` | 20 |
| **Borde: Procesamiento Total Borde** | `15.49` | `±13.78` | `38.0` | `6.18` | `38.0` | 20 |
| **Red Troncal: Tránsito RTT** | `14.6` | `±0.6` | `15.2` | `14.0` | `15.2` | 6 |
| **Servidor: LBP Entropía Textura** | `12.6` | `±1.07` | `13.97` | `11.0` | `15.62` | 20 |
| **Servidor: FFT Espectro Frecuencia** | `7.8` | `±0.3` | `8.1` | `7.5` | `8.1` | 6 |
| **Servidor: ArcFace Extracción 512d** | `265.4` | `±13.24` | `287.93` | `245.0` | `287.93` | 16 |
| **Servidor: ChromaDB Búsqueda Vectorial** | `3.53` | `±3.69` | `11.2` | `1.35` | `11.2` | 16 |
| **Servidor: SQLite Validación ACL/RBAC** | `147.77` | `±95.48` | `213.91` | `1.8` | `217.18` | 20 |
| **Servidor: Latencia Total Backend** | `391.48` | `±182.24` | `530.31` | `22.0` | `530.68` | 20 |
| **Latencia Total End-to-End** | **`411.35`** | **`±165.58`** | **`536.7`** | **`71.0`** | **`537.13`** | 20 |

---

## 6. Eficiencia de Auditoría Blockchain (Smart Contract en Ethereum)

- **Consumo de Gas Promedio (`logAuthentication`):** `182,844 gas` (Mín: `68,432` | Máx: `247,659`)
- **Tiempo de Sellado de Bloque (Sealing Time):** `60.51 ms` (`±34.26 ms` | P95: `115.4 ms`)
- **Total de Transacciones Notariadas en Cadena:** `20` eventos
