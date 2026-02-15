from abc import ABC, abstractmethod

class FileCompressible(ABC):
    @abstractmethod
    def compress_file(self, filename):
        pass
