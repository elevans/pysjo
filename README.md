pyops: Python wrapper for the SciJava Ops framework
===

pyops provides easy access to the SciJava Ops framework and helper classes to convert
between ImgLib2 and NumPy array types.

## Installation

With conda:

```bash
conda create -n pyops -c conda-forge imglyb scyjava openjdk>=11
```

With mamba

```bash
mamba create -n pyops imglyb scyjava openjdk>=11
```

Clone this repository, navigate to the `pyops` folder and install it with:

```bash
pip install -e .
```

## Usage

To access the Op environment, import `pyops` and use the `get_ops()` method:

```python
import pyops

# get an instance of the Op environment
ops = pyops.get_ops()
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
import pyops

# initialize the JVM with SciJava endpoints
pyops.init()
```
