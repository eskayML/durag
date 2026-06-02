import importlib.metadata

__version__ = importlib.metadata.version("durag")

from durag.memory.main import AsyncMemory, Memory  # noqa
