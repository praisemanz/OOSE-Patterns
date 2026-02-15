"""
IdleState - Concrete State for State Pattern
Represents the state when the machine is idle and waiting for money.
"""

from state import State
from product import Product


class IdleState(State):
    """State when the machine is idle and waiting for money"""
    
    def insert_money(self, amount: float) -> None:
        if amount <= 0:
            print("❌ Please insert a valid amount of money.")
            return
        
        print(f"✓ ${amount:.2f} inserted.")
        self._machine.add_to_balance(amount)
        print(f"💰 Current balance: ${self._machine.get_balance():.2f}")
        self._machine.set_state(self._machine.get_has_money_state())
    
    def select_product(self, product: Product) -> None:
        print("❌ Please insert money first.")
    
    def dispense(self) -> None:
        print("❌ Please insert money and select a product first.")
    
    def return_money(self) -> None:
        print("❌ No money to return.")
