import imglyb
import numpy as np
from pyops.java import imglib2

def imglib_to_numpy(rai: "net.imglib2.RandomAccessibleInterval", dtype="float64") -> np.ndarray:
    """Convert an ImgLib2 RandomAccessibleInterval to NumPy array.

    :param rai: Input RandomAccessibleInterval (RAI)
    :param dtype: dtype for output NumPy array (default=float64)
    :return: A NumPy array with the copied data and dtype
    """
    # create empty NumPy array
    shape = list(rai.dimensionsAsLongArray())
    shape.reverse() # XY -> row, col
    narr = np.zeros(shape, dtype=dtype)

    # create RAI reference with imglyb and compy data
    imglib2.ImgUtil.copy(rai, imglyb.to_imglib(narr))

    return narr


def numpy_to_imglib(narr: np.ndarray) -> "net.imglib2.RandomAccessibleInterval":
    """Convert a NumPy image to an ImgLib2 RandomAccessibleInterval.

    :param narr: Input NumPy array
    :return: An ImgLib2 RandomAccessibleInterval (reference)
    """
    return imglyb.to_imglib(narr)
