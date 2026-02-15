from abc import ABC, abstractmethod

class FileReadable(ABC):
    @abstractmethod
    def read_file(self, filename):
        pass
