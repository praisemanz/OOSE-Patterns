# Composite Pattern Implementation

## Pattern Description
The Composite pattern is a structural design pattern that allows you to compose objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly.

## Use Case: File System Hierarchy
This implementation models a file system with files and directories. Both files (leaf objects) and directories (composite objects) implement the same interface, allowing uniform treatment.

## Class Structure

### 1. **FileSystemComponent** (Abstract Component)
- **File**: `file_system_component.py`
- **Role**: Defines the common interface for both files and directories
- **Key Methods**:
  - `display(indent)`: Display the component
  - `get_size()`: Get the size of the component
  - `add(component)`: Add a child (throws error for leaves)
  - `remove(component)`: Remove a child (throws error for leaves)
  - `get_child(index)`: Get a child by index (throws error for leaves)

### 2. **File** (Leaf)
- **File**: `file.py`
- **Role**: Represents individual files (cannot have children)
- **Attributes**: `name`, `size`
- **Behavior**: Implements `display()` and `get_size()` for individual files

### 3. **Directory** (Composite)
- **File**: `directory.py`
- **Role**: Represents directories that can contain files and other directories
- **Attributes**: `name`, `children` (list of FileSystemComponents)
- **Behavior**: 
  - Can add/remove children
  - `display()` recursively displays all children
  - `get_size()` sums the sizes of all children

### 4. **Main Program**
- **File**: `main.py`
- **Purpose**: Demonstrates the pattern with a multi-level file system

## How the Code Adheres to the Pattern

1. **Uniform Interface**: Both `File` and `Directory` inherit from `FileSystemComponent`, providing the same interface
2. **Recursive Composition**: Directories can contain files and other directories, forming a tree structure
3. **Transparent Operations**: Operations like `get_size()` work the same way on both leaves and composites
4. **Client Simplicity**: The client code doesn't need to distinguish between files and directories

## Class Diagram Alignment

The class diagram shows:
- **Component**: `FileSystemComponent` (abstract base class)
- **Leaf**: `File` (cannot have children)
- **Composite**: `Directory` (can have children)
- **Inheritance**: Both File and Directory extend FileSystemComponent
- **Composition**: Directory contains 0 or more FileSystemComponents

## Running the Program

```bash
cd composite_pattern
python main.py
```

## Output
The program displays a tree structure showing:
- Nested directories and files
- Individual and total sizes
- Uniform treatment of files and directories

## Files in This Pattern
- `file_system_component.py` - Abstract Component
- `file.py` - Leaf class
- `directory.py` - Composite class
- `main.py` - Client code demonstrating the pattern
