import pysjo._addons
import pysjo._gateway as gateway


def get_ops():
    """Get an instance of the Ops Environment."""
    return gateway.get_ops_gateway()
