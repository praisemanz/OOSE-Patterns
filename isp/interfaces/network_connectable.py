from abc import ABC, abstractmethod

class NetworkConnectable(ABC):
    @abstractmethod
    def connect_to_server(self, ip, port):
        pass
