import scyjava as sj
import pyops
import pyops.convert as convert
from pyops.java import scifio

def open_as_img(path: str):
    """Open an image with SCIFIO as an ImgLib2 Img,
    """
    if not sj.jvm_started():
        pyops.init()

    opener = scifio.ImgOpener()

    return opener.openImg(path)


def open_as_numpy(path: str):
    """Open an imag with SCIFIO as a NumPy array,
    """
    if not sj.jvm_started():
        pyops.init()

    opener = scifio.ImgOpener()

    return convert.imglib_to_numpy(opener.openImg(path))
