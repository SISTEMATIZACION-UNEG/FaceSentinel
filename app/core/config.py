import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API
    PROJECT_NAME: str = "FaceSentinel"
    API_V1_STR: str = "/api/v1"
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # Rutas
    SQLITE_DB_PATH: str = os.getenv("SQLITE_DB_PATH", "./data/sql/database.db")
    CHROMA_DB_PATH: str = os.getenv("CHROMA_DB_PATH", "./data/chromadb")
    TEMP_IMAGES_PATH: str = os.getenv("TEMP_IMAGES_PATH", "./data/temp_images")
    
    # IA & Biometría
    AI_MODEL_NAME: str = os.getenv("AI_MODEL_NAME", "ArcFace")
    FACE_MATCH_THRESHOLD: float = float(os.getenv("FACE_MATCH_THRESHOLD", "0.60"))
    LIVENESS_POLICY: str = os.getenv("LIVENESS_POLICY", "passive_lbp")
    
    # Web3 & Red
    NETWORK_MODE: str = os.getenv("NETWORK_MODE", "host")
    BLOCKCHAIN_RPC_URL: str = os.getenv("BLOCKCHAIN_RPC_URL", os.getenv("WEB3_PROVIDER_URI", "http://127.0.0.1:5600"))
    CHAIN_ID: int = int(os.getenv("BLOCKCHAIN_CHAIN_ID") or os.getenv("CHAIN_ID", "963741852"))
    SMART_CONTRACT_ADDRESS: str = os.getenv("SMART_CONTRACT_ADDRESS") or os.getenv("CONTRACT_ADDRESS", "")
    DEVICE_PRIVATE_KEY: str = os.getenv("DEVICE_PRIVATE_KEY", "")
    # Cuenta administradora de la blockchain
    ADMIN_ADDRESS: str = os.getenv("BLOCKCHAIN_ACCOUNT") or os.getenv("ADMIN_ADDRESS", "")
    ADMIN_PRIVATE_KEY: str = os.getenv("BLOCKCHAIN_PRIVATE_KEY") or os.getenv("ADMIN_PRIVATE_KEY", "")

    # Seguridad — JWT
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "facesentinel-super-secret-key-change-in-production")
    JWT_EXPIRATION_MINUTES: int = int(os.getenv("JWT_EXPIRATION_MINUTES", "1440"))

    # Seguridad — Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 30

    # Seguridad — Anonimización de Usuario en Blockchain
    USER_ID_SALT: str = os.getenv("USER_ID_SALT", os.getenv("SALT_SECRETA", "facesentinel-secure-user-salt-key-2025"))

    # Seguridad M2M (Acceso Físico)
    HW_CLIENT_SECRET: str = "secret_door_01"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        # Ignorar variables del .env que no estén definidas en esta clase
        # (ej: WEB3_PROVIDER_URI, ADMIN_ADDRESS, ADMIN_PRIVATE_KEY son leídas por otros módulos con os.getenv)
        "extra": "ignore",
    }

# Creamos una instancia global para usarla en todo el proyecto
settings = Settings()

# Crear los directorios de datos automáticamente si no existen
os.makedirs(settings.TEMP_IMAGES_PATH, exist_ok=True)
os.makedirs(os.path.dirname(settings.SQLITE_DB_PATH), exist_ok=True)
os.makedirs(settings.CHROMA_DB_PATH, exist_ok=True)