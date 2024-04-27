import scyjava as sj
from pysjo.java import scijava
from typing import Sequence

# default SciJava Ops endpoints
sjo_endpoints = ["net.imglib2:imglib2",
        "net.imglib2:imglib2-imglyb",
        "io.scif:scifio",
        "org.scijava:scijava-ops-engine:0-SNAPSHOT",
        "org.scijava:scijava-ops-flim:0-SNAPSHOT",
        "org.scijava:scijava-ops-image:0-SNAPSHOT"]

def get_ops_gateway():
    """Get the SciJava Ops gateway.
    """
    return OpGateway()


def init(endpoints: Sequence[str]=None):
    """Configure and start the JVM with SciJava Ops

    :param endpoints: A list or tuple of endpoint strings
    """
    # add SciJava repository
    sj.config.add_repositories({"scijava.public": "https://maven.scijava.org/content/groups/public"})

    # add endpoints
    if not endpoints:
        sj.config.endpoints = sjo_endpoints
    else:
        sj.config.endpoints = endpoints

    # start the JVM
    sj.start_jvm()

class OpGateway:
    """SciJava Ops gateway
    """
    def __init__(self):
        if not sj.jvm_started():
            init()
        self.op_env = self._build_op_env()
        self.op_names = self._find_op_names()
        self.op_namespaces = self._find_op_namespaces()
        self.ops = None
        self._populate_op_gateway()

    def help(self, op_name=None):
        """Ops help.
        """
        if op_name:
            print(self.op_env.help(op_name), sep="\n")
        else:
            print(self.op_env.help(), sep = "\n")

    def _add_op(self, op_env: "scijava.OpEnvironment", op_name: str):
        return

    def _add_namespace(self, op_env: "scijava.OpEnvironment", op_namespace: str):
        return

    def _build_op_env(self):
        return scijava.OpEnvironment.build()

    def _find_op_names(self) -> set:
        return {str(name) for info in self.op_env.infos() for name in info.names()}

    def _find_op_namespaces(self) -> set:
        return {name.split(".")[0] for name in self.op_names}

    def _populate_op_gateway(self):
        # add namespaces to the gateway
        for ns in self.op_namespaces:
            setattr(self, ns, self.op_env)
