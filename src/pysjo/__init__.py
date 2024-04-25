import scyjava as sj
import pysjo._addons
from typing import Sequence

def get_ops():
    """Get an instance of the Ops Environment.
    """
    if not sj.jvm_started():
        init()

    return sj.jimport("org.scijava.ops.api.OpEnvironment").build()


def init(debug: bool=False):
    """Configure the JVM with a local build of the SciJava framework.
    """
    # add SciJava repository
    sj.config.add_repositories({"scijava.public": "https://maven.scijava.org/content/groups/public"})

    # add JVM options
    if debug:
        sj.config.add_option("-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=localhost:8300")

    # add endpoints
    sj.config.endpoints = ["net.imglib2:imglib2-imglyb",
            "io.scif:scifio"]

    # config JVM with local SciJava Ops jars
    sj.config.add_classpath(*sj.config.find_jars("/home/edward/Documents/workspaces/ops/sjo_jars"))

    # start the JVM
    sj.start_jvm()
