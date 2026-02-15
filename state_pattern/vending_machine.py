"""
VendingMachine - Context class for State Pattern
Maintains the current state and delegates operations to the state object.
"""

from product import Product
from state import State
from idle_state import IdleState
from has_money_state import HasMoneyState
from dispensing_state import DispensingState
from out_of_stock_state import OutOfStockState


class VendingMachine:
    """
    Context class that maintains the current state and delegates
    operations to the state object.
    """
    
    def __init__(self):
        # Initialize states
        self._idle_state = IdleState(self)
        self._has_money_state = HasMoneyState(self)
        self._dispensing_state = DispensingState(self)
        self._out_of_stock_state = OutOfStockState(self)
        
        # Set initial state
        self._current_state = self._idle_state
        
        # Machine properties
        self._balance = 0.0
        self._inventory = {
            Product.COLA: 5,
            Product.CHIPS: 3,
            Product.CANDY: 8,
            Product.WATER: 0  # Out of stock
        }
        self._selected_product = None
    
    # State transition methods
    def set_state(self, state: State) -> None:
        """Change the current state"""
        print(f"[STATE CHANGE] {self._current_state.__class__.__name__} -> {state.__class__.__name__}")
        self._current_state = state
    
    # Getter methods for states
    def get_idle_state(self) -> State:
        return self._idle_state
    
    def get_has_money_state(self) -> State:
        return self._has_money_state
    
    def get_dispensing_state(self) -> State:
        return self._dispensing_state
    
    def get_out_of_stock_state(self) -> State:
        return self._out_of_stock_state
    
    # Property accessors
    def add_to_balance(self, amount: float) -> None:
        self._balance += amount
    
    def get_balance(self) -> float:
        return self._balance
    
    def reset_balance(self) -> None:
        self._balance = 0.0
    
    def set_selected_product(self, product: Product) -> None:
        self._selected_product = product
    
    def get_selected_product(self) -> Product:
        return self._selected_product
    
    def get_inventory(self, product: Product) -> int:
        return self._inventory.get(product, 0)
    
    def reduce_inventory(self, product: Product) -> None:
        if self._inventory[product] > 0:
            self._inventory[product] -= 1
    
    def display_inventory(self) -> None:
        """Display current inventory"""
        print("\n--- INVENTORY ---")
        for product in Product:
            stock = self._inventory[product]
            status = "OUT OF STOCK" if stock == 0 else f"{stock} available"
            print(f"{product.product_name}: ${product.price:.2f} - {status}")
        print("-----------------\n")
    
    # Delegated operations to current state
    def insert_money(self, amount: float) -> None:
        """Insert money into the machine"""
        self._current_state.insert_money(amount)
    
    def select_product(self, product: Product) -> None:
        """Select a product"""
        self._current_state.select_product(product)
    
    def dispense(self) -> None:
        """Dispense the selected product"""
        self._current_state.dispense()
    
    def return_money(self) -> None:
        """Return the inserted money"""
        self._current_state.return_money()
