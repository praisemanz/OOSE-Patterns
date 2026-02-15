from abc import ABC, abstractmethod

class DataSendable(ABC):
    @abstractmethod
    def send_data(self, data):
        pass
