from pysjo.java import imglib2
from jpype import JImplementationFor

@JImplementationFor("net.imglib2.EuclideanSpace")
class EuclideanSpaceAddons(object):
    @property
    def ndim(self):
        """Get the number of dimensions.

        :return: Number of dimensions.
        """
        return self.numDimensions()

@JImplementationFor("net.imglib2.Interval")
class IntervalAddons(object):
    @property
    def shape(self):
        """Get the shape of the interval.

        :return: Tuple of the interval shape.
        """
        return tuple(self.dimension(d) for d in range(self.numDimensions()))

@JImplementationFor("net.imglib2.RandomAccessibleInterval")
class RAIAddons(object):
    @property
    def dtype(self):
        """Get the dtype of a RandomAccessibleInterval.

        :return: dtype of the RandomAccessibleInterval
        """
        return type(imglib2.Util.getTypeFromInterval(self))

