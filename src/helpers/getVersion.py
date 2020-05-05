# We use semantic versioning.
version = (0, 0, 1)

def changeVersion(newVersion: tuple) -> None:
    global version
    version = newVersion

def returnVersion() -> str:
    return "%.%.%" % version

version = returnVersion()