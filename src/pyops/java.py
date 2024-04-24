from scyjava import JavaClasses

class ImgLib2Classes(JavaClasses):
    """Easy access to ImgLib2 Java classes.
    """
    @JavaClasses.java_import
    def ImgUtil(self):
        return "net.imglib2.util.ImgUtil"

class SCIFIOClasses(JavaClasses):
    """Easy access to SCIFIO Java classes.
    """
    @JavaClasses.java_import
    def ImgOpener(self):
        return "io.scif.img.ImgOpener"

imglib2 = ImgLib2Classes()
scifio = SCIFIOClasses()
