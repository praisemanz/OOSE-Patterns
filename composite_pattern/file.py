"""
File - Leaf class for Composite Pattern
Represents individual files in the file system.
"""

from file_system_component import FileSystemComponent


class File(FileSystemComponent):
    """Leaf component representing a file"""
    
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size
    
    def display(self, indent: int = 0) -> None:
        """Display file with indentation"""
        print(f"{'  ' * indent}📄 {self.name} ({self.size} KB)")
    
    def get_size(self) -> int:
        """Return file size"""
        return self.size
