import pysjo._addons
import pysjo._gateway as gateway


def init(dir_or_endpoint = None):
    """Initialize an instance of the Ops Environment."""
    return gateway.init_ops_gateway(dir_or_endpoint)
