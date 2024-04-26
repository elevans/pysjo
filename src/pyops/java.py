from scyjava import JavaClasses

class ImgLib2Classes(JavaClasses):
    """Easy access to ImgLib2 Java classes.
    """
    # imglib2 numeric types
    @JavaClasses.java_import
    def BitType(self):
        return "net.imglib2.type.logic.BitType"

    @JavaClasses.java_import
    def BoolType(self):
        return "net.imglib2.type.logic.BoolType"

    @JavaClasses.java_import
    def ByteType(self):
        return "net.imglib2.type.numeric.integer.ByteType"

    @JavaClasses.java_import
    def ComplexDoubleType(self):
        return "net.imglib2.type.numeric.complex.ComplexDoubleType"

    @JavaClasses.java_import
    def ComplexFloatType(self):
        return "net.imglib2.type.numeric.complex.ComplexFloatType"

    @JavaClasses.java_import
    def DoubleType(self):
        return "net.imglib2.type.numeric.real.DoubleType"

    @JavaClasses.java_import
    def FloatType(self):
        return "net.imglib2.type.numeric.real.FloatType"

    @JavaClasses.java_import
    def UnsignedByteType(self):
        return "net.imglib2.type.numeric.integer.UnsignedByteType"

    @JavaClasses.java_import
    def UnsignedShortType(self):
        return "net.imglib2.type.numeric.integer.UnsignedShortType"

    # imglib2 utility classes
    @JavaClasses.java_import
    def ImgUtil(self):
        return "net.imglib2.util.ImgUtil"

    @JavaClasses.java_import
    def Util(self):
        return "net.imglib2.util.Util"

class SCIFIOClasses(JavaClasses):
    """Easy access to SCIFIO Java classes.
    """
    @JavaClasses.java_import
    def ImgOpener(self):
        return "io.scif.img.ImgOpener"

    @JavaClasses.java_import
    def ImgSaver(self):
        return "io.scif.img.ImgSaver"

imglib2 = ImgLib2Classes()
scifio = SCIFIOClasses()
