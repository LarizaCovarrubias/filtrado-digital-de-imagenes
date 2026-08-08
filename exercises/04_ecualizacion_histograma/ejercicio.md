# Ejercicio 04 — Ecualización de histograma

**Propósito:** implementación guiada.

Usa la fotografía principal en escala de grises y crea una versión de bajo contraste.

1. Calcula su histograma.
2. Obtén la PDF dividiendo el histograma entre el número total de píxeles.
3. Calcula la CDF con una suma acumulada.
4. Construye una LUT que lleve la CDF al intervalo `[0, 255]`.
5. Usa la LUT para generar la imagen ecualizada.
6. Compara visualmente tu resultado con `cv2.equalizeHist()`.
7. Explica qué papel cumplen PDF, CDF y LUT.

**Pista:** puedes seguir la misma secuencia `histograma → PDF → CDF → LUT` mostrada en el notebook 04.
