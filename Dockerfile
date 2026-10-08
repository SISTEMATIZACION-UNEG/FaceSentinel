# Base Image: Python 3.10 slim
FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# 1. Dependencias del sistema (Capa base fija en caché)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. CAPA PESADA INMUTABLE (TensorFlow, PyTorch, DeepFace, OpenCV)
# Esta capa se compilará UNA SOLA VEZ y Docker la dejará en caché permanente
COPY requirements-core.txt .
RUN pip install --timeout 120 --retries 5 --no-cache-dir -r requirements-core.txt

# 3. Pre-descargar pesos de ArcFace (Caché permanente junto a la capa pesada)
RUN python -c "from deepface import DeepFace; DeepFace.build_model('ArcFace')" || true

# 4. CAPA DINÁMICA (APIs, Web3, scikit-learn, etc.)
# Solo esta capa se reconstruirá cuando modifiques librerías secundarias (tarda ~10 seg)
COPY requirements.txt .
RUN pip install --timeout 60 --retries 5 --no-cache-dir -r requirements.txt

# 5. Código fuente de la aplicación (Se compila en 1 segundo cuando haces cambios de código)
COPY . .

# Asegurar directorios de persistencia
RUN mkdir -p /app/data/sql /app/data/chromadb /app/data/temp_images /app/data/logs /root/.deepface

EXPOSE 8000 8001

# Comprobación de salud
HEALTHCHECK --interval=30s --timeout=10s --start-period=35s --retries=3 \
    CMD curl -f http://localhost:${PORT:-8000}/ || exit 1

# Comando de inicio
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
