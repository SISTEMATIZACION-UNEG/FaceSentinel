"""
test_recognition.py — Tests unitarios para el servicio de reconocimiento facial
Verifica el flujo de registro, verificación, y almacenamiento.
"""

import os
import sys
import pytest
import numpy as np
import base64
import cv2

# Ajustar path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


# =========================================================================
#                       FIXTURES (Datos de prueba)
# =========================================================================

@pytest.fixture
def sample_image_base64():
    """Genera una imagen de prueba en Base64 (cuadro negro con un círculo blanco)."""
    img = np.zeros((200, 200, 3), dtype=np.uint8)
    # Dibujar un "rostro" básico para que OpenCV pueda procesarlo
    cv2.circle(img, (100, 80), 50, (200, 200, 200), -1)   # Cabeza
    cv2.circle(img, (85, 70), 8, (50, 50, 50), -1)         # Ojo izq
    cv2.circle(img, (115, 70), 8, (50, 50, 50), -1)        # Ojo der
    cv2.ellipse(img, (100, 100), (20, 10), 0, 0, 180, (100, 100, 100), 2)  # Boca
    _, buffer = cv2.imencode('.jpg', img)
    return base64.b64encode(buffer).decode('utf-8')


@pytest.fixture
def empty_image_base64():
    """Genera una imagen vacía (negra) sin ningún rostro."""
    img = np.zeros((200, 200, 3), dtype=np.uint8)
    _, buffer = cv2.imencode('.jpg', img)
    return base64.b64encode(buffer).decode('utf-8')


@pytest.fixture
def sample_embedding():
    """Genera un embedding facial simulado (vector de 512 dimensiones)."""
    np.random.seed(42)
    return np.random.randn(512).tolist()


# =========================================================================
#                    TESTS DE CONVERSIÓN DE IMAGEN
# =========================================================================

class TestImageConversion:
    """Tests para la conversión Base64 -> OpenCV."""

    def test_base64_to_image_valid(self, sample_image_base64):
        """Verifica que una imagen Base64 válida se convierte correctamente."""
        from app.services.face_recognition import base64_to_image

        img = base64_to_image(sample_image_base64)
        assert img is not None
        assert isinstance(img, np.ndarray)
        assert len(img.shape) == 3  # Debe tener 3 dimensiones (alto, ancho, canales)

    def test_base64_to_image_with_header(self, sample_image_base64):
        """Verifica que maneja correctamente el header data:image/jpeg;base64,..."""
        from app.services.face_recognition import base64_to_image

        img_with_header = f"data:image/jpeg;base64,{sample_image_base64}"
        img = base64_to_image(img_with_header)
        assert img is not None

    def test_base64_to_image_invalid(self):
        """Verifica que una imagen inválida lanza un error."""
        from app.services.face_recognition import base64_to_image

        with pytest.raises(Exception):
            base64_to_image("esto-no-es-base64-valido!!!")


# =========================================================================
#                    TESTS DE ALMACENAMIENTO
# =========================================================================

class TestStorage:
    """Tests para el servicio de almacenamiento (SQLite + ChromaDB)."""

    def test_save_and_retrieve_user(self, sample_embedding):
        """Verifica que se puede guardar y recuperar un usuario."""
        from app.services.storage import save_user_data, get_user_by_id

        user_id = "TEST-001"
        name = "Test User"
        role = "Tester"

        # Guardar
        result = save_user_data(user_id, name, role, sample_embedding)
        assert result is True

        # Recuperar
        user = get_user_by_id(user_id)
        assert user is not None
        assert user["name"] == name
        assert user["role"] == role

    def test_get_nonexistent_user(self):
        """Verifica que buscar un usuario que no existe retorna None."""
        from app.services.storage import get_user_by_id

        user = get_user_by_id("NO-EXISTE-99999")
        assert user is None

    def test_save_user_updates_existing(self, sample_embedding):
        """Verifica que guardar un usuario con ID existente lo actualiza."""
        from app.services.storage import save_user_data, get_user_by_id

        user_id = "TEST-UPDATE"

        save_user_data(user_id, "Nombre Original", "Rol1", sample_embedding)
        save_user_data(user_id, "Nombre Actualizado", "Rol2", sample_embedding)

        user = get_user_by_id(user_id)
        assert user["name"] == "Nombre Actualizado"
        assert user["role"] == "Rol2"


# =========================================================================
#                 TESTS DE PROCESAMIENTO DE IMAGEN
# =========================================================================

class TestImageProcessing:
    """Tests para el módulo de preprocesamiento de imagen."""

    def test_normalize_illumination(self, sample_image_base64):
        """Verifica que la normalización de iluminación funciona."""
        from app.utils.image_processing import normalize_illumination
        from app.services.face_recognition import base64_to_image

        img = base64_to_image(sample_image_base64)
        normalized = normalize_illumination(img)
        assert normalized is not None
        assert normalized.shape == img.shape

    def test_assess_quality_dark_image(self):
        """Verifica que detecta una imagen oscura."""
        from app.utils.image_processing import assess_image_quality

        dark_img = np.zeros((200, 200, 3), dtype=np.uint8)
        quality = assess_image_quality(dark_img)
        assert quality["brightness"] < 50
        assert "oscura" in " ".join(quality["issues"]).lower() or len(quality["issues"]) > 0

    def test_assess_quality_bright_image(self):
        """Verifica que detecta una imagen sobreexpuesta."""
        from app.utils.image_processing import assess_image_quality

        bright_img = np.ones((200, 200, 3), dtype=np.uint8) * 250
        quality = assess_image_quality(bright_img)
        assert quality["brightness"] > 200

    def test_decode_valid_base64(self, sample_image_base64):
        """Verifica la decodificación Base64 con validaciones."""
        from app.utils.image_processing import decode_base64_image

        img = decode_base64_image(sample_image_base64)
        assert img is not None
        assert img.shape[0] >= 100
        assert img.shape[1] >= 100


# =========================================================================
#                    TESTS DE LIVENESS
# =========================================================================

class TestLiveness:
    """Tests para el motor de anti-spoofing."""

    def test_analyze_texture_returns_dict(self, sample_image_base64):
        """Verifica que el análisis de textura retorna un resultado válido."""
        from app.services.liveness import analyze_texture
        from app.services.face_recognition import base64_to_image

        img = base64_to_image(sample_image_base64)
        result = analyze_texture(img)
        assert isinstance(result, dict)
        assert "texture_score" in result

    def test_analyze_frequency_returns_dict(self, sample_image_base64):
        """Verifica que el análisis de frecuencia retorna un resultado válido."""
        from app.services.liveness import analyze_frequency
        from app.services.face_recognition import base64_to_image

        img = base64_to_image(sample_image_base64)
        result = analyze_frequency(img)
        assert isinstance(result, dict)
        assert "frequency_score" in result

    def test_comprehensive_check_no_face(self):
        """Verifica que una imagen sin rostro falla el liveness y marca is_corrupted."""
        from app.services.liveness import comprehensive_liveness_check

        black_img = np.zeros((200, 200, 3), dtype=np.uint8)
        result = comprehensive_liveness_check(black_img)
        assert result["is_live"] is False
        assert result["is_corrupted"] is True

    def test_analyze_texture_corrupted_frame(self):
        """Verifica que un fotograma plano o dañado por red sea detectado como corrupto."""
        from app.services.liveness import analyze_texture

        black_img = np.zeros((128, 128, 3), dtype=np.uint8)
        result = analyze_texture(black_img)
        assert result["is_corrupted"] is True
        assert result["is_real"] is False
        assert result["entropy"] == 0.0


# =========================================================================
#                 TESTS DE VERIFICACIÓN 1:1 (CACHED & CANONICAL)
# =========================================================================

class TestOneToOneVerification:
    """Tests para la resolución canónica y matching 1:1 en memoria RAM."""

    def test_resolve_user_canonical(self):
        """Verifica que resolve_user_canonical encuentra usuarios por ID y username."""
        from app.services.storage import resolve_user_canonical

        # Usuario 'admin' existe en el sistema
        admin_info = resolve_user_canonical("admin")
        assert admin_info is not None
        assert admin_info["user_id"] == "admin"
        assert admin_info["name"] is not None

        # Usuario inexistente
        none_info = resolve_user_canonical("usuario_fantasma_xyz_123")
        assert none_info is None

        # String vacío o whitespace
        assert resolve_user_canonical("") is None
        assert resolve_user_canonical("   ") is None

    def test_get_user_reference_embeddings_indexed(self):
        """Verifica que get_user_reference_embeddings devuelve los embeddings del usuario de forma indexada."""
        from app.services.storage import get_user_reference_embeddings

        embs = get_user_reference_embeddings("admin")
        assert isinstance(embs, list)
        assert len(embs) >= 1
        assert len(embs[0]) == 512

        # Usuario sin biometría o inexistente
        no_embs = get_user_reference_embeddings("non_existent_user_id_456")
        assert isinstance(no_embs, list)
        assert len(no_embs) == 0

    def test_verify_face_1to1_cached_math(self):
        """Verifica el cálculo de similitud coseno mínima en RAM con vectores simulados."""
        from unittest.mock import patch
        from app.services.face_recognition import verify_face_1to1_cached

        # Vector de referencia sintético (L2 normalizado)
        ref_vec = np.random.randn(512).astype(np.float32)
        ref_vec = ref_vec / np.linalg.norm(ref_vec)
        cached_tensor = np.expand_dims(ref_vec, axis=0)  # Shape (1, 512)

        user_info = {
            "user_id": "test-uuid-canonical",
            "name": "Test User",
            "role": "Student"
        }

        # Caso A: Vector idéntico (distancia ~0.0 < umbral 0.45)
        with patch("app.services.face_recognition.get_embedding", return_value=(ref_vec.tolist(), 12.5)):
            dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
            res = verify_face_1to1_cached(dummy_img, cached_tensor, user_info, custom_threshold=0.45)
            assert res["success"] is True
            assert res["user_id"] == "test-uuid-canonical"
            assert res["distance"] < 0.05
            assert res["t_chroma_ms"] == 0.0

        # Caso B: Vector ortogonal/distinto (distancia ~1.0 >= umbral 0.45)
        diff_vec = np.random.randn(512).astype(np.float32)
        diff_vec = diff_vec / np.linalg.norm(diff_vec)
        # Forzar distancia alta
        diff_vec = -ref_vec
        with patch("app.services.face_recognition.get_embedding", return_value=(diff_vec.tolist(), 12.5)):
            dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
            res = verify_face_1to1_cached(dummy_img, cached_tensor, user_info, custom_threshold=0.45)
            assert res["success"] is False
            assert res["user_id"] == "test-uuid-canonical"
            assert res["distance"] > 0.45


# =========================================================================
#                    EJECUCIÓN
# =========================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])