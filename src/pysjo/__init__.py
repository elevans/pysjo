import pysjo._addons
import pysjo._gateway as gateway


def init():
    """Initialize an instance of the Ops Environment."""
    return gateway.init_ops_gateway()
