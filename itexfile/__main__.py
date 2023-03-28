import numpy
import numpy.typing
from os import PathLike

from .schema import FileType
from .read import read

def imread(path: PathLike) -> numpy.typing.NDArray:
    with open(path, mode="rb") as file:
        itex_image = read(file)
    dtype = numpy.uint16
    if itex_image.file_type == FileType.BIT8:
        dtype = numpy.uint8
    elif itex_image.file_type == FileType.BIT16:
        dtype = numpy.uint16
    elif itex_image.file_type == FileType.BIT32:
        dtype = numpy.uint32
    return numpy.frombuffer(itex_image.data, dtype=dtype).reshape((itex_image.height, itex_image.width))