import cv2
import numpy as np


def _kernel_binario(tamano: int) -> np.ndarray:
    if tamano < 1 or tamano % 2 == 0:
        raise ValueError("tamano debe ser impar y positivo")
    return np.ones((tamano, tamano), dtype=np.uint8)


def erosion_manual(imagen_binaria: np.ndarray, tamano: int = 3) -> np.ndarray:
    """Erosión binaria: el píxel queda blanco si toda la vecindad es blanca."""
    kernel = _kernel_binario(tamano)
    radio = tamano // 2
    binaria = imagen_binaria > 0
    padded = np.pad(binaria, radio, mode="constant", constant_values=False)
    salida = np.zeros_like(binaria)
    for i in range(binaria.shape[0]):
        for j in range(binaria.shape[1]):
            ventana = padded[i:i+tamano, j:j+tamano]
            salida[i, j] = np.all(ventana[kernel == 1])
    return salida.astype(np.uint8) * 255


def dilatacion_manual(imagen_binaria: np.ndarray, tamano: int = 3) -> np.ndarray:
    """Dilatación binaria: el píxel queda blanco si algún vecino es blanco."""
    kernel = _kernel_binario(tamano)
    radio = tamano // 2
    binaria = imagen_binaria > 0
    padded = np.pad(binaria, radio, mode="constant", constant_values=False)
    salida = np.zeros_like(binaria)
    for i in range(binaria.shape[0]):
        for j in range(binaria.shape[1]):
            ventana = padded[i:i+tamano, j:j+tamano]
            salida[i, j] = np.any(ventana[kernel == 1])
    return salida.astype(np.uint8) * 255


def apertura_manual(imagen_binaria: np.ndarray, tamano: int = 3) -> np.ndarray:
    return dilatacion_manual(erosion_manual(imagen_binaria, tamano), tamano)


def cierre_manual(imagen_binaria: np.ndarray, tamano: int = 3) -> np.ndarray:
    return erosion_manual(dilatacion_manual(imagen_binaria, tamano), tamano)


def erosion_opencv(imagen_binaria: np.ndarray, tamano: int = 3) -> np.ndarray:
    return cv2.erode(imagen_binaria, _kernel_binario(tamano), iterations=1)


def dilatacion_opencv(imagen_binaria: np.ndarray, tamano: int = 3) -> np.ndarray:
    return cv2.dilate(imagen_binaria, _kernel_binario(tamano), iterations=1)
