from enum import Enum

class FileType(Enum):
    folder = 0
    file = 1

class File:
    def __init__(self, name, path, content):
        self.name = name
        self.path = path
        self.content = content
        self.type = FileType.file

class Folder(File):
    def __init__(self, name, path, files):
        self.name = name
        self.path
        self.files = files
        self.type = FileType.folder
