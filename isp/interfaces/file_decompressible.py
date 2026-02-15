from abc import ABC, abstractmethod

class FileDecompressible(ABC):
    @abstractmethod
    def decompress_file(self, filename):
        pass
