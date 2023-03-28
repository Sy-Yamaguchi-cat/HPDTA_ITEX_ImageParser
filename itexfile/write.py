from typing import BinaryIO

from .schema import FileType, ITEXFile

def write(obj: ITEXFile, file: BinaryIO):
    file.write(b"IM")
    file.write(obj.comment_length.to_bytes(2, "little"))
    file.write(obj.width.to_bytes(2, "little"))
    file.write(obj.height.to_bytes(2, "little"))
    file.write(obj.x_offset.to_bytes(2, "little"))
    file.write(obj.y_offset.to_bytes(2, "little"))
    file.write(obj.file_type.to_bytes(2, "little"))
    file.write(obj.reserved)
    file.write(obj.comment)
    file.write(obj.data)
    