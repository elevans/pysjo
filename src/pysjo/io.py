import scyjava as sj
import pysjo
import pysjo.convert as convert
from pysjo.java import scifio

def open_as_img(path: str):
    """Open an image with SCIFIO as an ImgLib2 Img,
    """
    if not sj.jvm_started():
        pysjo.init()

    opener = scifio.ImgOpener()

    return opener.openImg(path)


def open_as_numpy(path: str):
    """Open an imag with SCIFIO as a NumPy array,
    """
    if not sj.jvm_started():
        pysjo.init()

    opener = scifio.ImgOpener()

    return convert.imglib_to_numpy(opener.openImg(path))


def save(path:str, image):
    """Save an image with SCIFIO.
    """
    if not sj.jvm_started():
        pysjo.init()

    if not sj.isjava(image):
        image = convert.numpy_to_imglib(image)

    saver = scifio.ImgSaver()
    saver.saveImg(path, image)