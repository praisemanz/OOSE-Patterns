from interfaces.file_readable import FileReadable
from interfaces.file_writable import FileWritable

class LocalFileManager(FileReadable, FileWritable):

    def read_file(self, filename):
        print(f"Reading {filename}")

    def write_file(self, filename, content):
        print(f"Writing to {filename}")
