"""
Main program for State Pattern demonstration
Demonstrates a vending machine with multiple operational states.
"""

from vending_machine import VendingMachine
from product import Product


def main():
    """Demonstrate the State pattern with various scenarios"""
    
    print("=" * 70)
    print("STATE PATTERN DEMONSTRATION - VENDING MACHINE")
    print("=" * 70)
    
    machine = VendingMachine()
    machine.display_inventory()
    
    # Scenario 1: Successful purchase
    print("\n" + "=" * 70)
    print("SCENARIO 1: Successful Purchase")
    print("=" * 70)
    machine.insert_money(2.00)
    machine.select_product(Product.COLA)
    
    # Scenario 2: Try to select without money
    print("\n" + "=" * 70)
    print("SCENARIO 2: Selecting Product Without Money")
    print("=" * 70)
    machine.select_product(Product.CHIPS)
    
    # Scenario 3: Insufficient funds
    print("\n" + "=" * 70)
    print("SCENARIO 3: Insufficient Funds")
    print("=" * 70)
    machine.insert_money(0.50)
    machine.select_product(Product.COLA)
    machine.insert_money(1.00)
    machine.select_product(Product.COLA)
    
    # Scenario 4: Return money
    print("\n" + "=" * 70)
    print("SCENARIO 4: Money Return")
    print("=" * 70)
    machine.insert_money(1.00)
    machine.return_money()
    
    # Scenario 5: Out of stock
    print("\n" + "=" * 70)
    print("SCENARIO 5: Out of Stock Product")
    print("=" * 70)
    machine.insert_money(2.00)
    machine.select_product(Product.WATER)
    machine.select_product(Product.CANDY)
    
    # Scenario 6: Multiple items
    print("\n" + "=" * 70)
    print("SCENARIO 6: Multiple Purchases")
    print("=" * 70)
    machine.insert_money(1.00)
    machine.select_product(Product.CHIPS)
    machine.insert_money(1.00)
    machine.select_product(Product.CANDY)
    
    # Final inventory
    machine.display_inventory()
    
    print("=" * 70)
    print("PATTERN BENEFITS DEMONSTRATED:")
    print("-" * 70)
    print("✓ Behavior changes based on internal state")
    print("✓ State transitions are explicit and controlled")
    print("✓ Each state encapsulates its own behavior")
    print("✓ New states can be added without modifying existing code")
    print("✓ Eliminates complex conditional statements")
    print("=" * 70)


if __name__ == "__main__":
    main()
