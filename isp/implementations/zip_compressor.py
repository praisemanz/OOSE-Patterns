from interfaces.file_compressible import FileCompressible
from interfaces.file_decompressible import FileDecompressible

class ZipCompressor(FileCompressible, FileDecompressible):

    def compress_file(self, filename):
        print(f"Compressing {filename}")

    def decompress_file(self, filename):
        print(f"Decompressing {filename}")
