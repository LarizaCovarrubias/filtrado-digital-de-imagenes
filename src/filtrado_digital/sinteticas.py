import numpy as np


def crear_rampa(ancho: int = 256, alto: int = 256) -> np.ndarray:
    """Genera una rampa horizontal de intensidades de 0 a 255."""
    fila = np.linspace(0, 255, ancho, dtype=np.uint8)
    return np.tile(fila, (alto, 1))


def crear_circulo(tamano: int = 256, radio: int = 70) -> np.ndarray:
    """Genera un círculo blanco sobre fondo negro."""
    yy, xx = np.ogrid[:tamano, :tamano]
    centro = tamano // 2
    mascara = (xx - centro) ** 2 + (yy - centro) ** 2 <= radio ** 2
    imagen = np.zeros((tamano, tamano), dtype=np.uint8)
    imagen[mascara] = 255
    return imagen


def crear_escena(tamano: int = 256) -> np.ndarray:
    """Genera una escena sintética con gradientes, figuras y diferentes contrastes."""
    y, x = np.mgrid[0:tamano, 0:tamano]
    base = 35 + 0.45 * x + 0.12 * y
    imagen = np.clip(base, 0, 255)

    # Rectángulo oscuro
    imagen[tamano//8:tamano//3, tamano//10:tamano//2] = 55
    # Rectángulo brillante
    imagen[tamano//2:tamano*3//4, tamano//2:tamano*9//10] = 210
    # Círculo de intensidad intermedia
    cx, cy, r = tamano*3//4, tamano//4, tamano//9
    mascara = (x-cx)**2 + (y-cy)**2 <= r**2
    imagen[mascara] = 145
    # Líneas delgadas para evaluar preservación de detalle
    imagen[tamano*4//5:tamano*4//5+2, tamano//12:tamano*5//12] = 235
    imagen[tamano//2:tamano*7//8, tamano//4:tamano//4+2] = 15
    return np.round(imagen).astype(np.uint8)


def agregar_ruido_gaussiano(imagen: np.ndarray, sigma: float = 20, semilla: int = 7) -> np.ndarray:
    """Agrega ruido Gaussiano reproducible."""
    rng = np.random.default_rng(semilla)
    ruido = rng.normal(0, sigma, imagen.shape)
    salida = imagen.astype(np.float64) + ruido
    return np.clip(salida, 0, 255).astype(np.uint8)


def agregar_ruido_sal_pimienta(imagen: np.ndarray, proporcion: float = 0.05, semilla: int = 7) -> np.ndarray:
    """Agrega ruido impulsivo sal y pimienta."""
    if not 0 <= proporcion <= 1:
        raise ValueError("proporcion debe estar entre 0 y 1")
    salida = imagen.copy()
    rng = np.random.default_rng(semilla)
    aleatorio = rng.random(imagen.shape)
    salida[aleatorio < proporcion / 2] = 0
    salida[(aleatorio >= proporcion / 2) & (aleatorio < proporcion)] = 255
    return salida
