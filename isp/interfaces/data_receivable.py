from abc import ABC, abstractmethod

class DataReceivable(ABC):
    @abstractmethod
    def receive_data(self):
        pass
