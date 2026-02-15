"""
Directory - Composite class for Composite Pattern
Represents directories that can contain files and other directories.
"""

from typing import List
from file_system_component import FileSystemComponent


class Directory(FileSystemComponent):
    """Composite component representing a directory"""
    
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []
    
    def add(self, component: FileSystemComponent) -> None:
        """Add a component to this directory"""
        self.children.append(component)
    
    def remove(self, component: FileSystemComponent) -> None:
        """Remove a component from this directory"""
        self.children.remove(component)
    
    def get_child(self, index: int) -> FileSystemComponent:
        """Get a child component by index"""
        return self.children[index]
    
    def display(self, indent: int = 0) -> None:
        """Display directory and all its contents recursively"""
        print(f"{'  ' * indent}📁 {self.name}/")
        for child in self.children:
            child.display(indent + 1)
    
    def get_size(self) -> int:
        """Calculate total size of directory (sum of all children)"""
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size
