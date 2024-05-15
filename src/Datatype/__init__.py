# For Python 3.8 and later
from importlib.metadata import version, PackageNotFoundError
try:
    __version__ = version("Datatype")
except PackageNotFoundError:
    # package is not installed
    __version__ = 'unknown'