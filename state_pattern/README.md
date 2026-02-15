# State Pattern Implementation

## Pattern Description
The State pattern is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. The object will appear to change its class. It eliminates complex conditional statements by encapsulating state-specific behavior in separate state objects.

## Use Case: Vending Machine
This implementation models a vending machine that changes behavior based on its current state: idle, has money, dispensing, or out of stock.

## Class Structure

### 1. **Product** (Enumeration)
- **File**: `product.py`
- **Role**: Defines available products with names and prices
- **Values**: COLA, CHIPS, CANDY, WATER

### 2. **VendingMachine** (Context)
- **File**: `vending_machine.py`
- **Role**: Maintains current state and delegates operations to state objects
- **Attributes**:
  - `_current_state`: Current state object
  - `_balance`: Current money balance
  - `_inventory`: Product stock levels
  - `_selected_product`: Currently selected product
- **Methods**:
  - `insert_money(amount)`: Delegates to current state
  - `select_product(product)`: Delegates to current state
  - `dispense()`: Delegates to current state
  - `return_money()`: Delegates to current state
  - `set_state(state)`: Changes the current state

### 3. **State** (Abstract State)
- **File**: `state.py`
- **Role**: Defines the interface for all concrete states
- **Methods**: `insert_money()`, `select_product()`, `dispense()`, `return_money()`

### 4. **Concrete States**

#### IdleState
- **File**: `idle_state.py`
- **State**: No money inserted, balance = $0
- **Behavior**: 
  - `insert_money()`: Transitions to HasMoneyState
  - Other operations: Display error messages

#### HasMoneyState
- **File**: `has_money_state.py`
- **State**: Money inserted, awaiting product selection
- **Behavior**:
  - `insert_money()`: Adds to balance (stays in same state)
  - `select_product()`: Checks stock and funds, transitions to DispensingState or OutOfStockState
  - `return_money()`: Returns balance, transitions to IdleState

#### DispensingState
- **File**: `dispensing_state.py`
- **State**: Product being dispensed
- **Behavior**:
  - `dispense()`: Dispenses product, returns change, transitions to IdleState
  - Other operations: Display "please wait" messages

#### OutOfStockState
- **File**: `out_of_stock_state.py`
- **State**: Selected product unavailable, money still in machine
- **Behavior**:
  - `select_product()`: Allows selecting alternative product
  - `return_money()`: Returns balance, transitions to IdleState

### 5. **Main Program**
- **File**: `main.py`
- **Purpose**: Demonstrates various scenarios and state transitions

## How the Code Adheres to the Pattern

1. **State Encapsulation**: Each state encapsulates its own behavior for all operations
2. **No Conditionals in Context**: VendingMachine doesn't use if/else to determine behavior
3. **State Transitions**: States themselves manage transitions to other states
4. **Context Reference**: Each state has a reference to the VendingMachine (context)
5. **Behavior Variation**: Same operation (e.g., `insert_money()`) behaves differently in different states

## Class Diagram Alignment

The class diagram shows:
- **Context**: `VendingMachine` (maintains current state)
- **State**: Abstract base class defining the interface
- **Concrete States**: IdleState, HasMoneyState, DispensingState, OutOfStockState
- **Relationships**:
  - Context has-a current State
  - Context knows all concrete states
  - All concrete states extend State
  - States have reference back to Context

## State Transitions

```
IdleState
    └─> insert_money() ──> HasMoneyState
    
HasMoneyState
    ├─> select_product(available, sufficient) ──> DispensingState
    ├─> select_product(unavailable) ──> OutOfStockState
    └─> return_money() ──> IdleState

DispensingState
    └─> dispense() ──> IdleState

OutOfStockState
    ├─> select_product(available) ──> HasMoneyState
    └─> return_money() ──> IdleState
```

## Running the Program

```bash
cd state_pattern
python main.py
```

## Output
The program demonstrates:
- Successful purchases with change
- Insufficient funds handling
- Out of stock scenarios
- Money return functionality
- State transitions (explicitly logged)
- Multiple purchase flows

## Benefits Demonstrated
- Behavior changes based on state
- No complex conditional logic
- Easy to add new states
- Each state's behavior is isolated
- State transitions are explicit and traceable

## Files in This Pattern
- `product.py` - Product enumeration
- `vending_machine.py` - Context class
- `state.py` - Abstract state class
- `idle_state.py` - Idle state implementation
- `has_money_state.py` - Has money state implementation
- `dispensing_state.py` - Dispensing state implementation
- `out_of_stock_state.py` - Out of stock state implementation
- `main.py` - Client code demonstrating the pattern
