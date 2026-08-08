import numpy as np
from .io import normalizar_uint8


def reflejo_horizontal_manual(imagen: np.ndarray) -> np.ndarray:
    """Refleja izquierda-derecha usando ciclos explícitos."""
    alto, ancho = imagen.shape[:2]
    salida = np.empty_like(imagen)
    for i in range(alto):
        for j in range(ancho):
            salida[i, ancho - 1 - j] = imagen[i, j]
    return salida


def reflejo_vertical_manual(imagen: np.ndarray) -> np.ndarray:
    """Refleja arriba-abajo usando ciclos explícitos."""
    alto, ancho = imagen.shape[:2]
    salida = np.empty_like(imagen)
    for i in range(alto):
        for j in range(ancho):
            salida[alto - 1 - i, j] = imagen[i, j]
    return salida


def rotar_90_manual(imagen: np.ndarray) -> np.ndarray:
    """Rota 90° en sentido antihorario mediante índices."""
    alto, ancho = imagen.shape[:2]
    nueva_forma = (ancho, alto) + (() if imagen.ndim == 2 else (imagen.shape[2],))
    salida = np.empty(nueva_forma, dtype=imagen.dtype)
    for i in range(alto):
        for j in range(ancho):
            salida[ancho - 1 - j, i] = imagen[i, j]
    return salida


def recortar(imagen: np.ndarray, fila_inicio: int, fila_fin: int, col_inicio: int, col_fin: int) -> np.ndarray:
    """Recorta una región mediante slicing de NumPy."""
    return imagen[fila_inicio:fila_fin, col_inicio:col_fin].copy()


def estadisticas_manual(imagen: np.ndarray) -> dict[str, float]:
    """Calcula media, varianza poblacional y desviación estándar con ciclos."""
    datos = imagen.astype(float).ravel()
    suma = 0.0
    for valor in datos:
        suma += valor
    media = suma / len(datos)
    acumulado = 0.0
    for valor in datos:
        acumulado += (valor - media) ** 2
    varianza = acumulado / len(datos)
    return {"media": media, "varianza": varianza, "desviacion": varianza ** 0.5}


def negativo(imagen: np.ndarray) -> np.ndarray:
    return 255 - imagen


def raiz_cuadrada(imagen: np.ndarray) -> np.ndarray:
    return normalizar_uint8(np.sqrt(imagen.astype(np.float64)))


def logaritmica(imagen: np.ndarray) -> np.ndarray:
    return normalizar_uint8(np.log1p(imagen.astype(np.float64)))
