import matplotlib.pyplot as plt
import numpy as np
from .histogramas import histograma_numpy


def mostrar_imagen(imagen: np.ndarray, titulo: str = "Imagen") -> None:
    plt.figure(figsize=(5, 5))
    if imagen.ndim == 2:
        plt.imshow(imagen, cmap="gray", vmin=0, vmax=255)
    else:
        plt.imshow(imagen)
    plt.title(titulo)
    plt.axis("off")
    plt.show()


def imagen_e_histograma(imagen: np.ndarray, titulo: str = "Imagen") -> None:
    hist = histograma_numpy(imagen)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    axes[0].imshow(imagen, cmap="gray", vmin=0, vmax=255)
    axes[0].set_title(titulo)
    axes[0].axis("off")
    axes[1].bar(np.arange(256), hist, width=1.0)
    axes[1].set_title("Histograma")
    axes[1].set_xlabel("Intensidad")
    axes[1].set_ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()


def comparar(imagenes: list[np.ndarray], titulos: list[str]) -> None:
    if len(imagenes) != len(titulos):
        raise ValueError("imagenes y titulos deben tener la misma longitud")
    fig, axes = plt.subplots(1, len(imagenes), figsize=(5 * len(imagenes), 4))
    if len(imagenes) == 1:
        axes = [axes]
    for ax, imagen, titulo in zip(axes, imagenes, titulos):
        if imagen.ndim == 2:
            ax.imshow(imagen, cmap="gray", vmin=0, vmax=255)
        else:
            ax.imshow(imagen)
        ax.set_title(titulo)
        ax.axis("off")
    plt.tight_layout()
    plt.show()
