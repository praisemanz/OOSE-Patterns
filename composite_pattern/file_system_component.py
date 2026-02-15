"""
FileSystemComponent - Abstract Component for Composite Pattern
Defines the interface for objects in the composition.
"""

from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    """Abstract component representing file system elements"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def display(self, indent: int = 0) -> None:
        """Display the component with indentation"""
        pass
    
    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the component"""
        pass
    
    def add(self, component: 'FileSystemComponent') -> None:
        """Add a child component (only valid for composites)"""
        raise NotImplementedError("Cannot add to a leaf component")
    
    def remove(self, component: 'FileSystemComponent') -> None:
        """Remove a child component (only valid for composites)"""
        raise NotImplementedError("Cannot remove from a leaf component")
    
    def get_child(self, index: int) -> 'FileSystemComponent':
        """Get a child component (only valid for composites)"""
        raise NotImplementedError("Leaf has no children")
