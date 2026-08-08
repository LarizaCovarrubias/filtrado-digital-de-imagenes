import cv2
import numpy as np

from .filtros import convolucion_2d_manual
from .io import normalizar_uint8


SOBEL_X = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
], dtype=np.float64)

SOBEL_Y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1],
], dtype=np.float64)

LAPLACIANO_4 = np.array([
    [0,  1, 0],
    [1, -4, 1],
    [0,  1, 0],
], dtype=np.float64)


def sobel_manual(imagen: np.ndarray, modo_borde: str = "reflect") -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Calcula gradientes Sobel Gx, Gy y magnitud normalizada."""
    gx = convolucion_2d_manual(imagen, SOBEL_X, modo_borde)
    gy = convolucion_2d_manual(imagen, SOBEL_Y, modo_borde)
    magnitud = np.hypot(gx, gy)
    return gx, gy, normalizar_uint8(magnitud)


def laplaciano_manual(imagen: np.ndarray, modo_borde: str = "reflect") -> np.ndarray:
    """Aplica un kernel Laplaciano y normaliza el valor absoluto a uint8."""
    respuesta = convolucion_2d_manual(imagen, LAPLACIANO_4, modo_borde)
    return normalizar_uint8(np.abs(respuesta))


def sobel_opencv(imagen: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    gx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    magnitud = normalizar_uint8(np.hypot(gx, gy))
    return gx, gy, magnitud


def laplaciano_opencv(imagen: np.ndarray) -> np.ndarray:
    respuesta = cv2.Laplacian(imagen, cv2.CV_64F, ksize=1)
    return normalizar_uint8(np.abs(respuesta))


def canny_opencv(imagen: np.ndarray, umbral_bajo: int = 80, umbral_alto: int = 160) -> np.ndarray:
    if not 0 <= umbral_bajo < umbral_alto <= 255:
        raise ValueError("Se requiere 0 <= umbral_bajo < umbral_alto <= 255")
    return cv2.Canny(imagen, umbral_bajo, umbral_alto)
