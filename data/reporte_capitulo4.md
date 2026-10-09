# FaceSentinel — Resultados Experimentales y Evaluación Científica del Capítulo IV

**Fecha de Evaluación:** 2026-10-08 20:03:22  
**Dataset Analizado:** `metricas_tesis.csv`  
**Total de Ensayos Registrados:** 30 intentos de autenticación

---

## 1. Matriz de Confusión Global de Control de Acceso

La siguiente matriz clasifica las decisiones del sistema entre accesos legítimos autorizados frente a intentos indebidos (ataques de presentación con foto/video e impostores no registrados):

| Condición Real \ Decisión Sistema | Acceso Concedido (GRANTED) | Acceso Denegado (DENIED) | Total Real |
|:---|:---:|:---:|:---:|
| **Sujeto Autorizado (Bona Fide Live)** | **Verdaderos Positivos (VP): 17** | **Falsos Negativos (FN): 5** | 22 |
| **Intento Indebido (Ataques + Impostores)** | **Falsos Positivos (FP): 0** | **Verdaderos Negativos (VN): 8** | 8 |
| **Total Clasificado** | 17 | 13 | **30** |

### Indicadores Globales de Seguridad
- **Exactitud General (Accuracy):** `83.33%`
- **Precisión (Precision):** `100.00%`
- **Sensibilidad / Tasa de Acierto (Recall / TPR):** `77.27%`
- **Especificidad (TNR):** `100.00%`
- **F1-Score:** `87.18%`
- **Tasa Global de Falsa Aceptación (FAR):** `0.00%` *(Vulnerabilidad de acceso)*
- **Tasa Global de Falso Rechazo (FRR):** `22.73%` *(Fricción de usuario)*

---

## 2. Evaluación Específica de Detección de Ataques de Presentación (PAD / ISO/IEC 30107-3)

Evaluación del subsistema Anti-Spoofing en el borde y servidor (MediaPipe Blink EAR + Textura LBP):

| Indicador PAD (ISO/IEC 30107-3) | Valor Obtenido | Muestras Evaluadas | Interpretación Técnica |
|:---|:---:|:---:|:---|
| **APCER - Fotos Impresas/Pantalla** | `0.00%` | 8 intentos | Fotos que burlaron la detección de liveness |
| **APCER - Video Replay con Parpadeo** | `0.00%` | 0 intentos | Videos en smartphone que lograron traspasar |
| **APCER Global (Ataques no detectados)** | **`0.00%`** | 8 ataques | Tasa total de filtración de ataques de presentación |
| **BPCER (Falso rechazo a vivos genuinos)**| **`4.55%`** | 22 intentos | Usuarios vivos confundidos erróneamente con spoofing |
| **ACER (Error Medio de Clasificación)**   | **`2.27%`** | 30 muestras | Media balanceada entre APCER y BPCER |

---

## 3. Evaluación del Reconocimiento Facial Biométrico (ISO/IEC 19795-1)

Rendimiento del modelo DeepFace ArcFace (512 dimensiones) con indexación vectorial ChromaDB (HNSW):

| Métrica Biometría Facial | Valor Obtenido | Muestras | Interpretación |
|:---|:---:|:---:|:---|
| **FNMR (False Non-Match Rate)** | `18.18%` | 22 | Usuarios autorizados vivos rechazados por distancia $d > 0.75$ |
| **FMR (False Match Rate)** | `0.00%` | 0 | Impostores vivos aceptados con distancia $d \le 0.75$ |
| **Distancia Coseno (Genuine Match)** | `0.11 ± 0.11` | 17 | Distancia promedio para accesos autorizados |
| **Distancia Coseno (Impostores/Desconocidos)** | `0.86 ± 0.04` | 4 | Distancia promedio para rostros no emparejados |

---

## 4. Análisis de Robustez ante Condiciones Ambientales (Iluminación)

| Entorno Evaluado | Muestras Totales | Decisiones Correctas | Fallos | Exactitud (%) | Latencia Media E2E (ms) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Iluminación Normal (Oficina/Lab)** | 22 | 17 | 5 | 77.27% | 441.14 ms |
| **Baja Iluminación (< 50 lux)** | 0 | 0 | 0 | 0.00% | 0.0 ms |
| **Alta Luz / Contraluz (> 1000 lux)** | 8 | 8 | 0 | 100.00% | 71.0 ms |

---

## 5. Benchmarking de Latencias del Pipeline (Milisegundos)

| Componente de Arquitectura | Media (ms) | Desv. Est. (ms) | Percentil 95 (ms) | Mín (ms) | Máx (ms) | Muestras |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Borde: MediaPipe Face Mesh (EAR)** | `13.69` | `±8.63` | `22.5` | `4.18` | `22.5` | 30 |
| **Borde: Procesamiento Total Borde** | `22.49` | `±15.02` | `38.0` | `6.18` | `38.0` | 30 |
| **Red Troncal: Tránsito RTT** | `14.6` | `±0.6` | `15.2` | `14.0` | `15.2` | 16 |
| **Servidor: LBP Entropía Textura** | `12.3` | `±1.05` | `13.97` | `11.0` | `15.62` | 30 |
| **Servidor: FFT Espectro Frecuencia** | `7.8` | `±0.3` | `8.1` | `7.5` | `8.1` | 16 |
| **Servidor: ArcFace Extracción 512d** | `260.54` | `±14.46` | `285.56` | `245.0` | `287.93` | 21 |
| **Servidor: ChromaDB Búsqueda Vectorial** | `5.36` | `±4.59` | `11.2` | `1.35` | `11.2` | 21 |
| **Servidor: SQLite Validación ACL/RBAC** | `99.16` | `±103.94` | `213.91` | `1.8` | `217.18` | 30 |
| **Servidor: Latencia Total Backend** | `312.16` | `±201.22` | `530.31` | `22.0` | `530.68` | 30 |
| **Latencia Total End-to-End** | **`342.43`** | **`±183.65`** | **`536.7`** | **`71.0`** | **`537.13`** | 30 |

---

## 6. Eficiencia de Auditoría Blockchain (Smart Contract en Ethereum)

- **Consumo de Gas Promedio (`logAuthentication`):** `144,707 gas` (Mín: `68,432` | Máx: `247,659`)
- **Tiempo de Sellado de Bloque (Sealing Time):** `77.91 ms` (`±37.29 ms` | P95: `115.4 ms`)
- **Total de Transacciones Notariadas en Cadena:** `30` eventos
