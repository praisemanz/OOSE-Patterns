"""Abstract class defining the template method"""
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    
    def process(self) -> None:
        """Template method - defines the algorithm skeleton"""
        self.read_data()
        self.process_data()
        self.validate_data()
        self.save_data()
        self._generate_report()
    
    def _generate_report(self) -> None:
        """Common implementation for all subclasses"""
        print("Generating processing report...")
        print("Report generated successfully.\n")
    
    @abstractmethod
    def read_data(self) -> None:
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def process_data(self) -> None:
        """Abstract method - must be implemented by subclasses"""
        pass
    
    def validate_data(self) -> None:
        """Hook method - optional override"""
        print("Performing basic data validation...")
    
    @abstractmethod
    def save_data(self) -> None:
        """Abstract method - must be implemented by subclasses"""
        pass
