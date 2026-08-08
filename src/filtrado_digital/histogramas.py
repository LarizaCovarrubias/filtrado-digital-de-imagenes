import numpy as np


def histograma_manual(imagen: np.ndarray) -> np.ndarray:
    """Cuenta manualmente cuántos píxeles existen para cada nivel [0,255]."""
    if imagen.ndim != 2:
        raise ValueError("histograma_manual espera una imagen en escala de grises")
    hist = np.zeros(256, dtype=np.int64)
    for valor in imagen.ravel():
        hist[int(valor)] += 1
    return hist


def histograma_numpy(imagen: np.ndarray) -> np.ndarray:
    """Histograma equivalente usando NumPy."""
    return np.bincount(imagen.ravel(), minlength=256)


def ecualizar_histograma_manual(imagen: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Ecualiza el histograma mediante PDF y CDF. Devuelve imagen y LUT."""
    hist = histograma_manual(imagen)
    pdf = hist / imagen.size
    cdf = np.cumsum(pdf)

    # Se usa el primer valor CDF no nulo para aprovechar mejor todo el rango.
    no_ceros = cdf[cdf > 0]
    if len(no_ceros) == 0:
        return imagen.copy(), np.arange(256, dtype=np.uint8)
    cdf_min = no_ceros[0]
    if cdf_min == 1:
        return imagen.copy(), np.arange(256, dtype=np.uint8)

    lut = np.round((cdf - cdf_min) / (1 - cdf_min) * 255)
    lut = np.clip(lut, 0, 255).astype(np.uint8)
    return lut[imagen], lut
