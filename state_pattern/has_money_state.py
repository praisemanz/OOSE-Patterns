"""
HasMoneyState - Concrete State for State Pattern
Represents the state when money has been inserted and machine awaits product selection.
"""

from state import State
from product import Product


class HasMoneyState(State):
    """State when money has been inserted and machine awaits product selection"""
    
    def insert_money(self, amount: float) -> None:
        if amount <= 0:
            print("❌ Please insert a valid amount of money.")
            return
        
        print(f"✓ ${amount:.2f} inserted.")
        self._machine.add_to_balance(amount)
        print(f"💰 Current balance: ${self._machine.get_balance():.2f}")
    
    def select_product(self, product: Product) -> None:
        # Check if product is in stock
        if self._machine.get_inventory(product) == 0:
            print(f"❌ {product.product_name} is out of stock.")
            self._machine.set_state(self._machine.get_out_of_stock_state())
            return
        
        # Check if balance is sufficient
        if self._machine.get_balance() < product.price:
            needed = product.price - self._machine.get_balance()
            print(f"❌ Insufficient funds. {product.product_name} costs ${product.price:.2f}.")
            print(f"   Please insert ${needed:.2f} more.")
            return
        
        print(f"✓ {product.product_name} selected (${product.price:.2f})")
        self._machine.set_selected_product(product)
        self._machine.set_state(self._machine.get_dispensing_state())
        
        # Automatically dispense after selection
        self._machine.dispense()
    
    def dispense(self) -> None:
        print("❌ Please select a product first.")
    
    def return_money(self) -> None:
        balance = self._machine.get_balance()
        print(f"💵 Returning ${balance:.2f}")
        self._machine.reset_balance()
        self._machine.set_state(self._machine.get_idle_state())
