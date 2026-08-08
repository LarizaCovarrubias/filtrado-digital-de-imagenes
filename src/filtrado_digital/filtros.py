import cv2
import numpy as np


def _validar_kernel_impar(tamano: int) -> None:
    if tamano < 1 or tamano % 2 == 0:
        raise ValueError("El tamaño del kernel debe ser un entero impar positivo.")


def _modo_padding(modo_borde: str) -> tuple[str, dict]:
    modos = {
        "zero": ("constant", {"constant_values": 0}),
        "replicate": ("edge", {}),
        "reflect": ("reflect", {}),
    }
    if modo_borde not in modos:
        raise ValueError("modo_borde debe ser 'zero', 'replicate' o 'reflect'.")
    return modos[modo_borde]


def convolucion_2d_manual(
    imagen: np.ndarray,
    kernel: np.ndarray,
    modo_borde: str = "reflect",
) -> np.ndarray:
    """Aplica una convolución 2D educativa y devuelve float64."""
    if imagen.ndim != 2:
        raise ValueError("convolucion_2d_manual espera una imagen 2D en grises")

    kernel = np.asarray(kernel, dtype=np.float64)
    if kernel.ndim != 2 or kernel.shape[0] % 2 == 0 or kernel.shape[1] % 2 == 0:
        raise ValueError("El kernel debe ser 2D y tener dimensiones impares.")

    radio_f = kernel.shape[0] // 2
    radio_c = kernel.shape[1] // 2
    modo_np, kwargs = _modo_padding(modo_borde)
    padded = np.pad(
        imagen.astype(np.float64),
        ((radio_f, radio_f), (radio_c, radio_c)),
        mode=modo_np,
        **kwargs,
    )

    # En la convolución matemática el kernel se invierte en ambos ejes.
    kernel_aplicado = np.flip(kernel, axis=(0, 1))

    salida = np.zeros(imagen.shape, dtype=np.float64)
    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):
            ventana = padded[i:i + kernel.shape[0], j:j + kernel.shape[1]]
            salida[i, j] = np.sum(ventana * kernel_aplicado)
    return salida


def filtro_promedio_manual(
    imagen: np.ndarray,
    tamano: int = 3,
    modo_borde: str = "reflect",
) -> np.ndarray:
    """Filtro promedio por convolución explícita."""
    _validar_kernel_impar(tamano)
    kernel = np.ones((tamano, tamano), dtype=np.float64) / (tamano * tamano)
    salida = convolucion_2d_manual(imagen, kernel, modo_borde)
    return np.clip(np.round(salida), 0, 255).astype(np.uint8)


def kernel_gaussiano(tamano: int = 5, sigma: float = 1.0) -> np.ndarray:
    """Construye un kernel Gaussiano 2D normalizado."""
    _validar_kernel_impar(tamano)
    if sigma <= 0:
        raise ValueError("sigma debe ser mayor que cero")
    radio = tamano // 2
    x = np.arange(-radio, radio + 1)
    xx, yy = np.meshgrid(x, x)
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return kernel / kernel.sum()


def filtro_gaussiano_manual(
    imagen: np.ndarray,
    tamano: int = 5,
    sigma: float = 1.0,
    modo_borde: str = "reflect",
) -> np.ndarray:
    """Aplica un filtro Gaussiano mediante convolución explícita."""
    kernel = kernel_gaussiano(tamano, sigma)
    salida = convolucion_2d_manual(imagen, kernel, modo_borde)
    return np.clip(np.round(salida), 0, 255).astype(np.uint8)


def filtro_mediana_manual(
    imagen: np.ndarray,
    tamano: int = 3,
    modo_borde: str = "reflect",
) -> np.ndarray:
    """Sustituye cada píxel por la mediana de su vecindad."""
    _validar_kernel_impar(tamano)
    radio = tamano // 2
    modo_np, kwargs = _modo_padding(modo_borde)
    padded = np.pad(imagen, radio, mode=modo_np, **kwargs)
    salida = np.zeros_like(imagen)
    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):
            ventana = padded[i:i + tamano, j:j + tamano]
            salida[i, j] = np.median(ventana)
    return salida


def filtro_promedio_opencv(imagen: np.ndarray, tamano: int = 3) -> np.ndarray:
    _validar_kernel_impar(tamano)
    return cv2.blur(imagen, (tamano, tamano))


def filtro_gaussiano_opencv(imagen: np.ndarray, tamano: int = 5, sigma: float = 1.0) -> np.ndarray:
    _validar_kernel_impar(tamano)
    return cv2.GaussianBlur(imagen, (tamano, tamano), sigmaX=sigma)


def filtro_mediana_opencv(imagen: np.ndarray, tamano: int = 3) -> np.ndarray:
    _validar_kernel_impar(tamano)
    return cv2.medianBlur(imagen, tamano)
