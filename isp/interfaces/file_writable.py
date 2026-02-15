from abc import ABC, abstractmethod

class FileWritable(ABC):
    @abstractmethod
    def write_file(self, filename, content):
        pass
