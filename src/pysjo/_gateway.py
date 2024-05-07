from types import MethodType
from typing import Sequence

import scyjava as sj

from pysjo.java import scijava

# default SciJava Ops endpoints
sjo_endpoints = [
    "net.imglib2:imglib2",
    "net.imglib2:imglib2-imglyb",
    "io.scif:scifio",
    "org.scijava:scijava-ops-engine:0-SNAPSHOT",
    "org.scijava:scijava-ops-flim:0-SNAPSHOT",
    "org.scijava:scijava-ops-image:0-SNAPSHOT",
]


class OpNamespace:
    """Op namespace class.

    Represents intermediate Ops categories and Ops. For example,
    "math.add" and "features.haralick.asm".
    """

    def __init__(self, env: "scijava.OpEnvironment", ns: str):
        self.op = env.op
        self._env = env
        self._ns = ns

    def help(self, op_name: str = None):
        """ """
        if op_name:
            print(self._env.help(op_name), sep="\n")
        else:
            print(self._env.help(), sep="\n")


class OpsGateway(OpNamespace):
    """SciJava Ops Gateway class.

    Contains all other namespaces, in addition to all Ops in
    the "global" namespace.
    """

    def __init__(self, env):
        super().__init__(env, "global")


def get_ops_gateway() -> OpsGateway:
    """Get the SciJava Ops Gateway.

    Initialize the JVM and return an instance of the
    SciJava Ops Gateway class.

    :return: The SciJava Ops Gateway.
    """
    if not sj.jvm_started():
        init()

    # build Ops environment and populate the gateway
    env = scijava.OpEnvironment.build()
    op_names = _find_op_names(env)
    for op in op_names:
        dot = op.find(".")
        if dot >= 0:
            ns = op[:dot]
            name = op[dot + 1 :]
            _add_namespace(OpsGateway, env, ns, name)
        else:
            _add_op(OpsGateway, env, op)

    return OpsGateway(env)


def init(endpoints: Sequence[str] = None):
    """Configure and start the JVM with SciJava Ops

    :param endpoints: A list or tuple of endpoint strings
    """
    # add SciJava repository
    sj.config.add_repositories(
        {"scijava.public": "https://maven.scijava.org/content/groups/public"}
    )

    # add endpoints
    if not endpoints:
        sj.config.endpoints = sjo_endpoints
    else:
        sj.config.endpoints = endpoints

    # start the JVM
    sj.start_jvm()


def _add_namespace(gc: OpsGateway, env: "scijava.OpEnvironment", ns: str, on: str):
    """Add an Op and it's namespace to the OpsGateway.

    Helper method to add an Op call with the appropriate nested
    OpNamespace instances if needed.

    :param gc: OpsGateway class
    :param env: SciJava Ops environment instance
    :param ns: Namespace
    :param on: Op name
    """
    if not hasattr(gc, ns):
        setattr(gc, ns, OpNamespace(env, ns))
    _add_op(getattr(gc, ns), env, on)


def _add_op(gc: OpsGateway, env: "scijava.OpEnvironment", on: str):
    """Add an Op to the OpsGateway.

    Helper method to add an Op with its corresponding function call
    to the given class.

    :param gc: OpsGateway class
    :param env: SciJava Ops environment instance
    :param on: Op name
    """
    if hasattr(gc, on):
        return

    def f(self, *args, **kwargs):
        """Op call instance methods.

        Instance method to attach to the OpNamespace/OpsGateway that does
        the actual Op call.
        """
        fqop = on if self._ns == "global" else self._ns + "." + on
        run = kwargs.get("run", True)
        req = env.op(fqop).input(*args)

        # inplace Op requests
        if (inplace := kwargs.get("inplace", None)) is not None:
            return req.mutate(inplace) if run else req.inplace(inplace)

        # computer Op requests
        if (out := kwargs.get("out", None)) is not None:
            req = req.output(out)
            return req.compute() if run else req.computer()

        # function Op requests
        return req.apply() if run else req.function()

    if gc == OpsGateway:
        # Op name is a global
        setattr(gc, on, f)
    else:
        m = MethodType(f, gc)
        setattr(gc, on, m)


def _find_op_names(env: "scijava.OpEnvironment") -> set:
    """Find all Op names in a SciJava Ops environment.

    :return: Set of all Op names/signatures
    """
    return {str(name) for info in env.infos() for name in info.names()}