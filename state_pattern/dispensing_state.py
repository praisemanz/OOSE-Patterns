"""
DispensingState - Concrete State for State Pattern
Represents the state when the machine is dispensing a product.
"""

from state import State
from product import Product


class DispensingState(State):
    """State when the machine is dispensing a product"""
    
    def insert_money(self, amount: float) -> None:
        print("❌ Please wait, dispensing product...")
    
    def select_product(self, product: Product) -> None:
        print("❌ Please wait, dispensing product...")
    
    def dispense(self) -> None:
        product = self._machine.get_selected_product()
        balance = self._machine.get_balance()
        
        print(f"🎁 Dispensing {product.product_name}...")
        self._machine.reduce_inventory(product)
        
        # Calculate change
        change = balance - product.price
        if change > 0:
            print(f"💵 Returning change: ${change:.2f}")
        
        print(f"✓ Enjoy your {product.product_name}!")
        
        # Reset machine state
        self._machine.reset_balance()
        self._machine.set_selected_product(None)
        self._machine.set_state(self._machine.get_idle_state())
    
    def return_money(self) -> None:
        print("❌ Cannot return money while dispensing.")
