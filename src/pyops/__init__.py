import scyjava as sj

def init():
    """Initialize a SciJava Ops environment.
    """
    # add SciJava repository
    sj.config.add_repositories({"scijava.public": "https://maven.scijava.org/content/groups/public"})

    # add endpoints
    sj.config.endpoints = ["net.imglib2:imglib2",
            "net.imglib2:imglib2-imglyb",
            "io.scif:scifio",
            "org.scijava:scijava-ops-engine:0-SNAPSHOT",
            "org.scijava:scijava-ops-image:0-SNAPSHOT"]

    return sj.jimport("org.scijava.ops.api.OpEnvironment").build()
