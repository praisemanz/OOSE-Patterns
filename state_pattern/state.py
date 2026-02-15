"""
State - Abstract State class for State Pattern
Defines the interface for all concrete states.
"""

from abc import ABC, abstractmethod
from product import Product


class State(ABC):
    """Abstract state class defining the interface for all concrete states"""
    
    def __init__(self, machine: 'VendingMachine'):
        self._machine = machine
    
    @abstractmethod
    def insert_money(self, amount: float) -> None:
        """Handle money insertion"""
        pass
    
    @abstractmethod
    def select_product(self, product: Product) -> None:
        """Handle product selection"""
        pass
    
    @abstractmethod
    def dispense(self) -> None:
        """Handle product dispensing"""
        pass
    
    @abstractmethod
    def return_money(self) -> None:
        """Handle money return"""
        pass
