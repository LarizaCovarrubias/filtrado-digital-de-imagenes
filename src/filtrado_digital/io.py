from pathlib import Path
import cv2
import numpy as np


def raiz_proyecto() -> Path:
    """Localiza la raíz del repositorio desde Jupyter, VS Code o la terminal."""
    candidatos = [Path.cwd(), *Path.cwd().parents]
    for base in candidatos:
        if (base / "pyproject.toml").exists() and (base / "src" / "filtrado_digital").exists():
            return base

    base = Path(__file__).resolve().parents[2]
    if (base / "pyproject.toml").exists():
        return base

    raise FileNotFoundError(
        "No se encontró la raíz del proyecto. Ejecuta el notebook dentro del repositorio."
    )


def ruta_imagen_ejemplo(nombre: str = "imagen_principal.jpg") -> Path:
    """Devuelve la ruta a una imagen incluida en ``images/samples``."""
    ruta = raiz_proyecto() / "images" / "samples" / nombre
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró la imagen de ejemplo: {ruta}")
    return ruta


def cargar_imagen(ruta: str | Path) -> np.ndarray:
    """Carga una imagen en RGB desde disco."""
    ruta = Path(ruta)
    imagen_bgr = cv2.imread(str(ruta), cv2.IMREAD_COLOR)
    if imagen_bgr is None:
        raise FileNotFoundError(f"No se pudo leer la imagen: {ruta}")
    return cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2RGB)


def a_grises(imagen: np.ndarray) -> np.ndarray:
    """Convierte una imagen RGB a escala de grises; deja intacta una imagen 2D."""
    if imagen.ndim == 2:
        return imagen.copy()
    if imagen.ndim == 3 and imagen.shape[2] == 3:
        return cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
    raise ValueError("Se esperaba una imagen 2D o RGB de tres canales.")


def normalizar_uint8(matriz: np.ndarray) -> np.ndarray:
    """Escala una matriz al intervalo [0, 255] y la convierte a uint8."""
    datos = matriz.astype(np.float64)
    minimo = datos.min()
    maximo = datos.max()
    if maximo == minimo:
        return np.zeros_like(datos, dtype=np.uint8)
    normalizada = (datos - minimo) / (maximo - minimo)
    return np.round(normalizada * 255).astype(np.uint8)
