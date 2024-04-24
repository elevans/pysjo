import scyjava as sj
import pyops._addons
from typing import Sequence

def get_ops():
    """Get an instance of the Ops Environment.
    """
    if not sj.jvm_started():
        init()

    return sj.jimport("org.scijava.ops.api.OpEnvironment").build()


def init(endpoints: Sequence[str]=None):
    """Configure and start the JVM with SciJava Ops

    :param endpoints: A list or tuple of endpoint strings
    """
    # add SciJava repository
    sj.config.add_repositories({"scijava.public": "https://maven.scijava.org/content/groups/public"})

    # add endpoints
    if not endpoints:
        sj.config.endpoints = ["net.imglib2:imglib2",
                "net.imglib2:imglib2-imglyb",
                "io.scif:scifio",
                "org.scijava:scijava-ops-engine:0-SNAPSHOT",
                "org.scijava:scijava-ops-flim:0-SNAPSHOT",
                "org.scijava:scijava-ops-image:0-SNAPSHOT"]

    # start the JVM
    sj.start_jvm()
