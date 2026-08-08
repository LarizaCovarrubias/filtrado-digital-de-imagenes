import cv2
import numpy as np
from .histogramas import histograma_manual


def umbral_global_manual(imagen: np.ndarray, umbral: int = 127) -> np.ndarray:
    """Binariza una imagen con un umbral fijo."""
    salida = np.zeros_like(imagen, dtype=np.uint8)
    salida[imagen > umbral] = 255
    return salida


def calcular_otsu_manual(imagen: np.ndarray) -> int:
    """Calcula el umbral de Otsu maximizando la varianza entre clases."""
    hist = histograma_manual(imagen).astype(np.float64)
    prob = hist / hist.sum()
    niveles = np.arange(256)
    media_total = np.sum(niveles * prob)
    peso_fondo = 0.0
    media_acum = 0.0
    mejor_varianza = -1.0
    mejor_umbral = 0

    for t in range(256):
        peso_fondo += prob[t]
        media_acum += t * prob[t]
        peso_objeto = 1.0 - peso_fondo
        if peso_fondo == 0 or peso_objeto == 0:
            continue
        media_fondo = media_acum / peso_fondo
        media_objeto = (media_total - media_acum) / peso_objeto
        varianza_entre = peso_fondo * peso_objeto * (media_fondo - media_objeto) ** 2
        if varianza_entre > mejor_varianza:
            mejor_varianza = varianza_entre
            mejor_umbral = t
    return mejor_umbral


def otsu_manual(imagen: np.ndarray) -> tuple[int, np.ndarray]:
    umbral = calcular_otsu_manual(imagen)
    return umbral, umbral_global_manual(imagen, umbral)


def umbral_adaptativo_media_manual(imagen: np.ndarray, tamano: int = 11, c: float = 2.0) -> np.ndarray:
    """Umbral local basado en la media de una ventana."""
    if tamano < 3 or tamano % 2 == 0:
        raise ValueError("tamano debe ser impar y >= 3")
    radio = tamano // 2
    padded = np.pad(imagen, radio, mode="reflect")
    salida = np.zeros_like(imagen, dtype=np.uint8)
    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):
            ventana = padded[i:i+tamano, j:j+tamano]
            umbral_local = float(np.mean(ventana)) - c
            salida[i, j] = 255 if imagen[i, j] > umbral_local else 0
    return salida


def otsu_opencv(imagen: np.ndarray) -> tuple[float, np.ndarray]:
    return cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
