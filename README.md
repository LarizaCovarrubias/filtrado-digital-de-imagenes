# Filtrado digital de imágenes con Python

Repositorio educativo en español para aprender **procesamiento y filtrado digital de imágenes** desde un nivel introductorio.

El recorrido combina explicaciones intuitivas, implementaciones paso a paso y comparaciones con herramientas de uso común como **NumPy** y **OpenCV**. La intención no es únicamente aprender a llamar funciones, sino comprender qué ocurre con los píxeles, cómo funciona cada técnica y en qué situaciones puede ser útil.

![Fotografía principal del repositorio](images/samples/imagen_principal.jpg)

## ¿A quién está dirigido?

Este repositorio está pensado para estudiantes y personas que desean comenzar a trabajar con imágenes digitales utilizando Python.

No se requiere experiencia previa en procesamiento digital de imágenes. Sin embargo, se recomienda conocer fundamentos básicos de Python, por ejemplo:

- variables y tipos de datos;
- condicionales;
- ciclos;
- funciones;
- listas;
- importación de módulos.

Los conceptos específicos de imágenes, matrices, histogramas, filtros y segmentación se introducen progresivamente a lo largo de los notebooks.

## Objetivo

Al terminar el recorrido podrás:

- comprender cómo una imagen digital se representa como una matriz;
- interpretar conceptos como píxel, intensidad, `shape`, `dtype` y canales de color;
- seleccionar y reorganizar regiones mediante índices y *slicing*;
- analizar la distribución de intensidades mediante histogramas;
- aplicar transformaciones de intensidad;
- mejorar el contraste global y local mediante ecualización y CLAHE;
- comprender el funcionamiento de la convolución, el *padding* y los kernels;
- comparar filtros de suavizado frente a distintos tipos de ruido;
- detectar bordes con Sobel, Laplaciano y Canny;
- segmentar imágenes mediante técnicas de umbralización;
- aplicar operaciones morfológicas sobre imágenes binarias;
- elegir técnicas básicas de procesamiento según el problema y analizar sus resultados.

## Ruta de aprendizaje

Se recomienda seguir los módulos en orden, ya que algunos conceptos se reutilizan posteriormente.

| Módulo | Tema | Notebook |
| --- | --- | --- |
| 01 | Imágenes como matrices | [`01_imagenes_como_matrices.ipynb`](notebooks/01_imagenes_como_matrices.ipynb) |
| 02 | Operaciones básicas y *slicing* | [`02_operaciones_basicas.ipynb`](notebooks/02_operaciones_basicas.ipynb) |
| 03 | Histogramas y transformaciones de intensidad | [`03_histogramas_y_transformaciones.ipynb`](notebooks/03_histogramas_y_transformaciones.ipynb) |
| 04 | Ecualización de histograma | [`04_ecualizacion_histograma.ipynb`](notebooks/04_ecualizacion_histograma.ipynb) |
| 05 | CLAHE | [`05_clahe.ipynb`](notebooks/05_clahe.ipynb) |
| 06 | Ruido y filtros de suavizado | [`06_filtros_suavizado.ipynb`](notebooks/06_filtros_suavizado.ipynb) |
| 07 | Detección de bordes | [`07_deteccion_bordes.ipynb`](notebooks/07_deteccion_bordes.ipynb) |
| 08 | Umbralización | [`08_umbralizacion.ipynb`](notebooks/08_umbralizacion.ipynb) |
| 09 | Operaciones morfológicas | [`09_operaciones_morfologicas.ipynb`](notebooks/09_operaciones_morfologicas.ipynb) |

## Metodología de aprendizaje

Los módulos siguen, cuando el tema lo permite, una secuencia común:

1. **Comprender el concepto.** Se introduce qué problema resuelve la técnica y qué significan los términos necesarios.
2. **Observar un ejemplo.** Se trabaja con matrices pequeñas, imágenes sintéticas o una fotografía real.
3. **Implementar paso a paso.** Algunas operaciones se construyen manualmente para comprender el algoritmo.
4. **Visualizar el resultado.** Se comparan imágenes, histogramas u otras representaciones.
5. **Usar herramientas existentes.** Se muestran alternativas con NumPy u OpenCV cuando corresponde.
6. **Interpretar.** Se analiza qué cambió, por qué ocurrió y cuándo podría utilizarse la técnica.

En términos generales:

```text
comprender → implementar → visualizar → comparar → interpretar
```

Las implementaciones manuales priorizan la **claridad educativa** sobre la velocidad de ejecución.

## Inicio rápido

### Opción 1 — Crear el entorno Conda recomendado

Desde la carpeta raíz del proyecto:

```bash
conda env create -f environment.yml
conda activate filtrado-digital
pip install -e .
jupyter lab
```

`environment.yml` crea el entorno de trabajo con Python, JupyterLab y las herramientas necesarias para ejecutar y validar el proyecto.

`pip install -e .` instala el paquete `filtrado_digital` en modo editable y agrega las dependencias Python definidas en `pyproject.toml`.

Una vez abierto JupyterLab, entra a `notebooks/` y comienza con:

```text
01_imagenes_como_matrices.ipynb
```

Ejecuta las celdas en orden y modifica los ejemplos cuando quieras experimentar.

### Opción 2 — Utilizar un entorno Conda existente

Si ya tienes un entorno Conda:

```bash
conda activate NOMBRE_DE_TU_ENTORNO
conda install -c conda-forge jupyterlab ipykernel pytest pip
pip install -e .
jupyter lab
```

### ¿Qué hace `pip install -e .`?

La opción `-e` significa **editable**.

Permite que los notebooks utilicen las funciones ubicadas en `src/filtrado_digital/` mediante imports normales:

```python
from filtrado_digital.filtros import filtro_gaussiano_manual
```

Si modificas el código de `src/`, los cambios quedan disponibles para el proyecto sin tener que reinstalarlo después de cada modificación.

## Cómo está organizado el proyecto

```text
filtrado-digital-imagenes-python/
├── notebooks/             # Lecciones principales
├── exercises/             # Ejercicios y soluciones explicadas
├── src/
│   └── filtrado_digital/  # Código reutilizable usado por los notebooks
├── images/                # Imágenes de ejemplo y licencias
├── tests/                 # Pruebas automáticas
├── environment.yml        # Entorno recomendado para Conda
├── pyproject.toml         # Configuración y dependencias del proyecto
├── .gitignore
├── LICENSE
└── README.md
```

Para estudiar el contenido, principalmente utilizarás:

```text
notebooks/   → aprender
exercises/   → practicar
images/      → recursos utilizados en los ejemplos
```

Las carpetas `src/` y `tests/` forman parte de la organización interna y del mantenimiento del proyecto.

## Notebooks y `src/`

Los notebooks contienen las explicaciones, ejemplos y experimentos.

La carpeta `src/filtrado_digital/` contiene funciones reutilizables que pueden utilizarse desde diferentes notebooks. Por ejemplo:

```python
from filtrado_digital.filtros import filtro_gaussiano_manual
```

importa una función definida en:

```text
src/filtrado_digital/filtros.py
```

Normalmente no necesitas ejecutar los archivos de `src/` directamente: los notebooks los utilizan mediante `import`.

## Ejercicios adicionales

Cada módulo cuenta con una actividad práctica independiente. Se recomienda intentar resolverla **después de completar el notebook correspondiente y antes de abrir la solución**.

```text
exercises/
├── 01_imagenes_como_matrices/
│   ├── ejercicio.md
│   └── solucion.ipynb
├── 02_operaciones_basicas/
│   ├── ejercicio.md
│   └── solucion.ipynb
└── ...
```

Cada ejercicio puede centrarse en **implementación**, **aplicación y análisis**, o una combinación de ambos.

En general, las actividades buscan desarrollar tres habilidades:

```text
programar → visualizar → interpretar
```

Las soluciones están en formato `.ipynb` para poder incluir código, imágenes, histogramas, comparaciones y explicaciones.

Cada solución es independiente y puede ejecutarse con `Run All` una vez que el proyecto está instalado con `pip install -e .`.

## Imágenes de ejemplo

La fotografía principal utilizada en varios módulos se encuentra en:

```text
images/samples/imagen_principal.jpg
```

Su procedencia y licencia están documentadas en [`images/README.md`](images/README.md).

También se utilizan imágenes sintéticas cuando permiten controlar mejor el ejemplo, por ejemplo para explicar matrices, ruido, kernels y operaciones morfológicas.

## Utilizar imágenes propias

Puedes crear:

```text
images/personal/
```

y colocar ahí tus propias fotografías para experimentar con los métodos del repositorio.

Esta carpeta está ignorada por Git para evitar que las imágenes personales se publiquen accidentalmente.

## Pruebas automáticas

La carpeta `tests/` contiene pruebas para comprobar que las principales funciones de `src/` continúan funcionando correctamente después de realizar modificaciones.

Desde la raíz del proyecto:

```bash
pytest
```

Las pruebas no son necesarias para estudiar las lecciones, pero ayudan a mantener la calidad del código.

## Uso en VS Code

Los notebooks `.ipynb` pueden abrirse directamente en VS Code utilizando las extensiones **Python** y **Jupyter**.

Selecciona el mismo entorno Conda donde instalaste el proyecto con:

```bash
pip install -e .
```

Los imports utilizados en JupyterLab funcionarán de la misma manera.

## Google Colab

El proyecto también puede utilizarse en Google Colab. Una vez publicado en GitHub:

```python
!git clone <URL-DE-TU-REPOSITORIO>
%cd filtrado-digital-imagenes-python
!pip install -e .
```

Después de la instalación, los mismos imports utilizados en JupyterLab y VS Code estarán disponibles en Colab.

## Alcance actual

Esta primera parte se centra en **procesamiento de imágenes en el dominio espacial**.

Incluye fundamentos de representación, intensidad, contraste, convolución, suavizado, detección de bordes, umbralización y morfología.

La **Transformada de Fourier** y el **filtrado en el dominio de frecuencia** quedan fuera del alcance actual y pueden incorporarse posteriormente como una segunda parte del proyecto.

## Licencia

El código y el material educativo del repositorio se distribuyen bajo licencia MIT.

Las imágenes de terceros conservan sus propias condiciones de uso. La información correspondiente está documentada en [`images/README.md`](images/README.md).
