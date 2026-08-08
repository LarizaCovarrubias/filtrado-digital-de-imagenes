# Imágenes del repositorio

Este repositorio combina una **fotografía real con licencia clara** y algunas imágenes sintéticas generadas por el propio código.

## Fotografía principal

Archivo: `samples/imagen_principal.jpg`

- **Título original:** *Landscape of Nature*
- **Autor:** Yasir 48
- **Fuente:** Wikimedia Commons
- **Licencia:** CC0 1.0 Universal (dedicación al dominio público)
- **Página de origen:** https://commons.wikimedia.org/wiki/File:Landscape_of_Nature.jpg
- **Versión incluida:** derivado de 1280 px servido por Wikimedia Commons, renombrado como `imagen_principal.jpg`.

CC0 permite copiar, modificar y redistribuir la obra, incluso con fines comerciales, sin solicitar permiso. Aunque la atribución no es obligatoria bajo CC0, se conserva aquí para documentar el origen del recurso.

## Imágenes sintéticas

`rampa.png` y `circulo.png` se generan con funciones de `src/filtrado_digital/sinteticas.py` y se usan cuando una figura controlada ayuda a explicar un concepto.

Puedes regenerarlas con:

```bash
python scripts/generate_sample_images.py
```

## Imágenes personales

Si deseas experimentar con fotografías propias, puedes crear `images/personal/`. Esa carpeta está ignorada por Git para evitar subir archivos personales accidentalmente.
