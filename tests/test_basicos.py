import numpy as np

from filtrado_digital.sinteticas import crear_rampa, crear_circulo
from filtrado_digital.histogramas import histograma_manual, histograma_numpy
from filtrado_digital.transformaciones import reflejo_horizontal_manual
from filtrado_digital.thresholding import umbral_global_manual
from filtrado_digital.filtros import convolucion_2d_manual
from filtrado_digital.bordes import sobel_manual


def test_rampa():
    img = crear_rampa(256, 10)
    assert img.shape == (10, 256)
    assert img.dtype == np.uint8
    assert img[0, 0] == 0
    assert img[0, -1] == 255


def test_histogramas_coinciden():
    img = crear_circulo(64, 15)
    assert np.array_equal(histograma_manual(img), histograma_numpy(img))


def test_reflejo_manual():
    img = np.arange(12, dtype=np.uint8).reshape(3, 4)
    assert np.array_equal(reflejo_horizontal_manual(img), img[:, ::-1])


def test_umbral():
    img = np.array([[0, 100, 200]], dtype=np.uint8)
    out = umbral_global_manual(img, 127)
    assert np.array_equal(out, np.array([[0, 0, 255]], dtype=np.uint8))


def test_convolucion_identidad():
    img = np.arange(25, dtype=np.uint8).reshape(5, 5)
    kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=float)
    out = convolucion_2d_manual(img, kernel)
    assert np.array_equal(out, img.astype(float))


def test_sobel_detecta_transicion():
    img = np.zeros((32, 32), dtype=np.uint8)
    img[:, 16:] = 255
    gx, gy, mag = sobel_manual(img)
    assert mag.shape == img.shape
    assert mag.dtype == np.uint8
    assert mag[:, 15:17].max() == 255
    assert np.abs(gx[:, 15:17]).max() > 0


def test_imagen_principal_disponible():
    from filtrado_digital.io import cargar_imagen, ruta_imagen_ejemplo
    ruta = ruta_imagen_ejemplo()
    imagen = cargar_imagen(ruta)
    assert ruta.name == "imagen_principal.jpg"
    assert imagen.ndim == 3
    assert imagen.shape[2] == 3
    assert imagen.dtype == np.uint8
