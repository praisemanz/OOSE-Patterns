"""
Product - Enumeration for State Pattern
Defines available products in the vending machine.
"""

from enum import Enum


class Product(Enum):
    """Available products in the vending machine"""
    COLA = ("Cola", 1.50)
    CHIPS = ("Chips", 1.00)
    CANDY = ("Candy", 0.75)
    WATER = ("Water", 1.25)
    
    def __init__(self, name: str, price: float):
        self.product_name = name
        self.price = price
