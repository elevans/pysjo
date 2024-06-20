import pysjo._addons
import pysjo._gateway as gateway
from typing import Sequence


def init(endpoints: Sequence[str] = None):
    """Initialize an instance of the Ops Environment."""
    return gateway.init_ops_gateway()
