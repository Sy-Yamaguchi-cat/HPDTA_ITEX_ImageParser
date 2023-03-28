
from enum import IntEnum
from configparser import ConfigParser

ConfigParser().items()

class FileType(IntEnum):
    BIT8 = 0
    COMPRESSED = 1
    BIT16 = 2
    BIT32 = 3


class ITEXFile:
    comment_length: int
    width: int
    height: int
    x_offset: int
    y_offset: int
    file_type: FileType
    reserved: bytes
    comment: bytes
    data: bytes

    def __init__(self,
        comment_length: int,
        width: int,
        height: int,
        x_offset: int,
        y_offset: int,
        file_type: FileType,
        reserved: bytes,
        comment: bytes,
        data: bytes
    ) -> None:
        self.comment_length = comment_length
        self.width = width
        self.height = height
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.file_type = file_type
        self.reserved = reserved
        self.comment = comment
        self.data = data

    @getattr
    def user_comment(self) -> str:
        config = ConfigParser()
        config.read_string(self.comment.decode("utf-8"))
        return config["Comment"]["UserComment"]

