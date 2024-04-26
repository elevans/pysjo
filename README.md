pysjo: Python wrapper for the SciJava Ops framework
===

pysjo provides easy access to the SciJava Ops framework and helper classes to convert
between ImgLib2 and NumPy array types.

## Installation

With conda:

```bash
conda create -n pysjo -c conda-forge imglyb scyjava openjdk>=11
```

With mamba

```bash
mamba create -n pysjo imglyb scyjava openjdk>=11
```

Clone this repository, navigate to the `pysjo` folder and install it with:

```bash
pip install -e .
```

## Usage

### Initialize SciJava Ops
To access the Op environment, import `pysjo` and use the `get_ops()` method:

```python
import pysjo

# get an instance of the Op environment
ops = pysjo.get_ops()
```

We can check that the Ops environment build was successful by printing the output of `ops.help()`:

```
>>> ops.help()
'Namespaces:
	> coloc
	> convert
	> copy
	> create
	> deconvolve
	> expression
	> features
	> filter
	> flim
	> geom
	> image
	> imageMoments
	> labeling
	> linalg
	> logic
	> map
	> math
	> morphology
	> segment
	> stats
	> thread
	> threshold
	> topology
	> transform
	> types'
```

You can also start the JVM configured for the SciJava Ops framework (_i.e._ the default endpoints)
without building the Op environment by using the `init()` method instead:

```python
import pysjo

# initialize the JVM with SciJava endpoints
pysjo.init()
```

### Opening and saving images

Images can be opened and saved using the `pysjo.io` module (backed by SCIFIO): 

```python
import pysjo.io as io

# open data as Img
img = io.open_as_img("/path/to/data.tif")

# open data as NumPy
narr = io.open_as_numpy("/path/to/data/tif")
```

### Converting between ImgLib2 and NumPy images

Images can be converted between ImgLib2 (_i.e._ `net.imglib2.RandomAccessibleInterval`) and
NumPy (_i.e._ `numpy.ndarray`) with the `pysjo.convert` module:

```python
import pysjo.convert as convert

# convert an Img to a NumPy array
narr = convert.imglib_to_numpy(img)

# convert a NumPy array to an Img/RAI
img = convert.numpy_to_imglib(narr)
```

### Accessing ImgLib2 and SciJava classes

Commonly used Java classes for ImgLib2, SCIFIO and other related projects
can be accessed through the `pysjo.java` module:

```python
from pysjo.java import imglib2, scifio

# access ImgLib2
imglib2.ComplexFloatType
imglib2.DoubleType
imglib2.Img

# access scifio
scifio.ImgOpener
scifio.ImgSaver
```
