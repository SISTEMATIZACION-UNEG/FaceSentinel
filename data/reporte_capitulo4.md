# FaceSentinel — Resultados Experimentales y Evaluación Científica del Capítulo IV

**Fecha de Evaluación:** 2026-10-05 19:18:15  
**Dataset Analizado:** `metricas_tesis.csv`  
**Total de Ensayos Registrados:** 16 intentos de autenticación

---

## 1. Matriz de Confusión Global de Control de Acceso

La siguiente matriz clasifica las decisiones del sistema entre accesos legítimos autorizados frente a intentos indebidos (ataques de presentación con foto/video e impostores no registrados):

| Condición Real \ Decisión Sistema | Acceso Concedido (GRANTED) | Acceso Denegado (DENIED) | Total Real |
|:---|:---:|:---:|:---:|
| **Sujeto Autorizado (Bona Fide Live)** | **Verdaderos Positivos (VP): 10** | **Falsos Negativos (FN): 5** | 15 |
| **Intento Indebido (Ataques + Impostores)** | **Falsos Positivos (FP): 0** | **Verdaderos Negativos (VN): 1** | 1 |
| **Total Clasificado** | 10 | 6 | **16** |

### Indicadores Globales de Seguridad
- **Exactitud General (Accuracy):** `68.75%`
- **Precisión (Precision):** `100.00%`
- **Sensibilidad / Tasa de Acierto (Recall / TPR):** `66.67%`
- **Especificidad (TNR):** `100.00%`
- **F1-Score:** `80.00%`
- **Tasa Global de Falsa Aceptación (FAR):** `0.00%` *(Vulnerabilidad de acceso)*
- **Tasa Global de Falso Rechazo (FRR):** `33.33%` *(Fricción de usuario)*

---

## 2. Evaluación Específica de Detección de Ataques de Presentación (PAD / ISO/IEC 30107-3)

Evaluación del subsistema Anti-Spoofing en el borde y servidor (MediaPipe Blink EAR + Textura LBP):

| Indicador PAD (ISO/IEC 30107-3) | Valor Obtenido | Muestras Evaluadas | Interpretación Técnica |
|:---|:---:|:---:|:---|
| **APCER - Fotos Impresas/Pantalla** | `0.00%` | 1 intentos | Fotos que burlaron la detección de liveness |
| **APCER - Video Replay con Parpadeo** | `0.00%` | 0 intentos | Videos en smartphone que lograron traspasar |
| **APCER Global (Ataques no detectados)** | **`0.00%`** | 1 ataques | Tasa total de filtración de ataques de presentación |
| **BPCER (Falso rechazo a vivos genuinos)**| **`6.67%`** | 15 intentos | Usuarios vivos confundidos erróneamente con spoofing |
| **ACER (Error Medio de Clasificación)**   | **`3.33%`** | 16 muestras | Media balanceada entre APCER y BPCER |

---

## 3. Evaluación del Reconocimiento Facial Biométrico (ISO/IEC 19795-1)

Rendimiento del modelo DeepFace ArcFace (512 dimensiones) con indexación vectorial ChromaDB (HNSW):

| Métrica Biometría Facial | Valor Obtenido | Muestras | Interpretación |
|:---|:---:|:---:|:---|
| **FNMR (False Non-Match Rate)** | `26.67%` | 15 | Usuarios autorizados vivos rechazados por distancia $d > 0.75$ |
| **FMR (False Match Rate)** | `0.00%` | 0 | Impostores vivos aceptados con distancia $d \le 0.75$ |
| **Distancia Coseno (Genuine Match)** | `0.03 ± 0.07` | 10 | Distancia promedio para accesos autorizados |
| **Distancia Coseno (Impostores/Desconocidos)** | `0.86 ± 0.04` | 4 | Distancia promedio para rostros no emparejados |

---

## 4. Análisis de Robustez ante Condiciones Ambientales (Iluminación)

| Entorno Evaluado | Muestras Totales | Decisiones Correctas | Fallos | Exactitud (%) | Latencia Media E2E (ms) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Iluminación Normal (Oficina/Lab)** | 15 | 10 | 5 | 66.67% | 489.18 ms |
| **Baja Iluminación (< 50 lux)** | 0 | 0 | 0 | 0.00% | 0.0 ms |
| **Alta Luz / Contraluz (> 1000 lux)** | 1 | 1 | 0 | 100.00% | 71.0 ms |

---

## 5. Benchmarking de Latencias del Pipeline (Milisegundos)

| Componente de Arquitectura | Media (ms) | Desv. Est. (ms) | Percentil 95 (ms) | Mín (ms) | Máx (ms) | Muestras |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Borde: MediaPipe Face Mesh (EAR)** | `6.64` | `±5.72` | `22.5` | `4.18` | `22.5` | 16 |
| **Borde: Procesamiento Total Borde** | `10.24` | `±9.94` | `38.0` | `6.18` | `38.0` | 16 |
| **Red Troncal: Tránsito RTT** | `14.6` | `±0.6` | `15.2` | `14.0` | `15.2` | 2 |
| **Servidor: LBP Entropía Textura** | `12.83` | `±1.03` | `15.62` | `11.0` | `15.62` | 16 |
| **Servidor: FFT Espectro Frecuencia** | `7.8` | `±0.3` | `8.1` | `7.5` | `8.1` | 2 |
| **Servidor: ArcFace Extracción 512d** | `268.32` | `±11.51` | `287.93` | `245.0` | `287.93` | 14 |
| **Servidor: ChromaDB Búsqueda Vectorial** | `2.44` | `±2.45` | `11.2` | `1.35` | `11.2` | 14 |
| **Servidor: SQLite Validación ACL/RBAC** | `184.22` | `±68.93` | `217.18` | `1.8` | `217.18` | 16 |
| **Servidor: Latencia Total Backend** | `450.98` | `±139.62` | `530.68` | `22.0` | `530.68` | 16 |
| **Latencia Total End-to-End** | **`463.04`** | **`±128.27`** | **`537.13`** | **`71.0`** | **`537.13`** | 16 |

---

## 6. Eficiencia de Auditoría Blockchain (Smart Contract en Ethereum)

- **Consumo de Gas Promedio (`logAuthentication`):** `211,448 gas` (Mín: `68,432` | Máx: `247,659`)
- **Tiempo de Sellado de Bloque (Sealing Time):** `47.47 ms` (`±24.79 ms` | P95: `115.4 ms`)
- **Total de Transacciones Notariadas en Cadena:** `16` eventos
