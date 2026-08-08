# Ejercicio 02 — Operaciones básicas

**Propósito:** implementación.

Usa la fotografía principal en escala de grises.

1. Selecciona con *slicing* un recorte cuadrado de `160 × 160` píxeles.
2. Implementa con ciclos un reflejo horizontal del recorte.
3. Compara tu resultado con `recorte[:, ::-1]`.
4. Crea una máscara rectangular que conserve solo la región central del recorte y visualízala.
5. Calcula la media del recorte con un ciclo y compárala con `np.mean()`.
6. Explica qué parte del ejercicio usa índices y qué parte usa *slicing*.
