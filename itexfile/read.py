from .schema import ITEXFile, FileType

from typing import BinaryIO

def read(file: BinaryIO) -> ITEXFile:
    check = file.read(2)
    if check != b"IM":
        raise RuntimeError("ITEX image file should start widh \"IM\".")
    comment_length = int.from_bytes(file.read(2), "little")
    width = int.from_bytes(file.read(2), "little")
    height = int.from_bytes(file.read(2), "little")
    x_offset = int.from_bytes(file.read(2), "little")
    y_offset = int.from_bytes(file.read(2), "little")
    file_type = FileType(int.from_bytes(file.read(2), "little"))
    reserved = file.read(64 - 14)
    comment = file.read(comment_length)
    data = file.read()
    return ITEXFile(
        comment_length=comment_length,
        width=width,
        height=height,
        x_offset=x_offset,
        y_offset=y_offset,
        file_type=file_type,
        reserved=reserved,
        comment=comment,
        data=data,
    )
