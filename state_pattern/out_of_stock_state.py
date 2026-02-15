"""
OutOfStockState - Concrete State for State Pattern
Represents the state when the selected product is out of stock.
"""

from state import State
from product import Product


class OutOfStockState(State):
    """State when the selected product is out of stock"""
    
    def insert_money(self, amount: float) -> None:
        if amount <= 0:
            print("❌ Please insert a valid amount of money.")
            return
        
        print(f"✓ ${amount:.2f} inserted.")
        self._machine.add_to_balance(amount)
        print(f"💰 Current balance: ${self._machine.get_balance():.2f}")
        self._machine.set_state(self._machine.get_has_money_state())
    
    def select_product(self, product: Product) -> None:
        if self._machine.get_inventory(product) == 0:
            print(f"❌ {product.product_name} is still out of stock. Please select another product.")
        else:
            self._machine.set_state(self._machine.get_has_money_state())
            self._machine.select_product(product)
    
    def dispense(self) -> None:
        print("❌ Cannot dispense. Product is out of stock.")
    
    def return_money(self) -> None:
        balance = self._machine.get_balance()
        if balance > 0:
            print(f"💵 Returning ${balance:.2f}")
            self._machine.reset_balance()
        else:
            print("❌ No money to return.")
        self._machine.set_state(self._machine.get_idle_state())
