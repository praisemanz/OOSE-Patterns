"""
Binary Tree Implementation using Composite Pattern
Demonstrates how Composite pattern naturally maps to tree structures
"""

from abc import ABC, abstractmethod
from typing import Optional


# Component
class TreeNode(ABC):
    """Abstract base class for tree nodes (Component)"""
    
    def __init__(self, value):
        self.value = value
    
    @abstractmethod
    def display(self, prefix: str = "", is_tail: bool = True) -> str:
        """Display the tree structure"""
        pass
    
    @abstractmethod
    def get_height(self) -> int:
        """Get the height of the tree"""
        pass
    
    @abstractmethod
    def count_nodes(self) -> int:
        """Count total nodes in tree"""
        pass
    
    @abstractmethod
    def sum_values(self) -> int:
        """Sum all values in tree"""
        pass
    
    @abstractmethod
    def inorder(self) -> list:
        """Inorder traversal: left -> root -> right"""
        pass
    
    @abstractmethod
    def preorder(self) -> list:
        """Preorder traversal: root -> left -> right"""
        pass
    
    @abstractmethod
    def postorder(self) -> list:
        """Postorder traversal: left -> right -> root"""
        pass


# Leaf
class LeafNode(TreeNode):
    """Leaf node - has no children (Leaf in Composite pattern)"""
    
    def display(self, prefix: str = "", is_tail: bool = True) -> str:
        connector = "└── " if is_tail else "├── "
        return f"{prefix}{connector}🍃 {self.value}"
    
    def get_height(self) -> int:
        return 0
    
    def count_nodes(self) -> int:
        return 1
    
    def sum_values(self) -> int:
        return self.value
    
    def inorder(self) -> list:
        """Leaf node inorder is just the value"""
        return [self.value]
    
    def preorder(self) -> list:
        """Leaf node preorder is just the value"""
        return [self.value]
    
    def postorder(self) -> list:
        """Leaf node postorder is just the value"""
        return [self.value]


# Composite
class BinaryNode(TreeNode):
    """Binary tree node - can have left and right children (Composite)"""
    
    def __init__(self, value):
        super().__init__(value)
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
    
    def set_left(self, node: TreeNode) -> None:
        """Add left child"""
        self.left = node
    
    def set_right(self, node: TreeNode) -> None:
        """Add right child"""
        self.right = node
    
    def display(self, prefix: str = "", is_tail: bool = True) -> str:
        """Display tree structure using box-drawing characters"""
        result = []
        
        # Current node
        connector = "└── " if is_tail else "├── "
        if prefix == "":
            result.append(f"🌳 {self.value}")
        else:
            result.append(f"{prefix}{connector}🔵 {self.value}")
        
        # Prepare prefix for children
        extension = "    " if is_tail else "│   "
        new_prefix = prefix + extension
        
        # Display children
        if self.left is not None or self.right is not None:
            if self.right is not None:
                result.append(self.right.display(new_prefix, False))
            else:
                result.append(f"{new_prefix}├── ∅")
            
            if self.left is not None:
                result.append(self.left.display(new_prefix, True))
            else:
                result.append(f"{new_prefix}└── ∅")
        
        return "\n".join(result)
    
    def get_height(self) -> int:
        """Calculate tree height"""
        left_height = self.left.get_height() if self.left else -1
        right_height = self.right.get_height() if self.right else -1
        return 1 + max(left_height, right_height)
    
    def count_nodes(self) -> int:
        """Count all nodes in subtree"""
        left_count = self.left.count_nodes() if self.left else 0
        right_count = self.right.count_nodes() if self.right else 0
        return 1 + left_count + right_count
    
    def sum_values(self) -> int:
        """Sum all values in subtree"""
        left_sum = self.left.sum_values() if self.left else 0
        right_sum = self.right.sum_values() if self.right else 0
        return self.value + left_sum + right_sum
    
    def inorder(self) -> list:
        """Inorder traversal: left -> root -> right"""
        result = []
        if self.left:
            result.extend(self.left.inorder())
        result.append(self.value)
        if self.right:
            result.extend(self.right.inorder())
        return result
    
    def preorder(self) -> list:
        """Preorder traversal: root -> left -> right"""
        result = [self.value]
        if self.left:
            result.extend(self.left.preorder())
        if self.right:
            result.extend(self.right.preorder())
        return result
    
    def postorder(self) -> list:
        """Postorder traversal: left -> right -> root"""
        result = []
        if self.left:
            result.extend(self.left.postorder())
        if self.right:
            result.extend(self.right.postorder())
        result.append(self.value)
        return result


def create_sample_tree() -> BinaryNode:
    """Create a sample binary tree"""
    #           10
    #          /  \
    #         5    15
    #        / \   / \
    #       3   7 12  20
    #      /         \
    #     1          25
    
    root = BinaryNode(10)
    
    # Left subtree
    left = BinaryNode(5)
    left.set_left(BinaryNode(3))
    if isinstance(left.left, BinaryNode):
        left.left.set_left(LeafNode(1))
    left.set_right(LeafNode(7))
    
    # Right subtree
    right = BinaryNode(15)
    right.set_left(LeafNode(12))
    right.set_right(BinaryNode(20))
    if isinstance(right.right, BinaryNode):
        right.right.set_right(LeafNode(25))
    
    root.set_left(left)
    root.set_right(right)
    
    return root


def create_balanced_tree() -> BinaryNode:
    """Create a balanced binary tree"""
    #        50
    #       /  \
    #     25    75
    #    / \    / \
    #   10 30  60 80
    
    root = BinaryNode(50)
    
    left = BinaryNode(25)
    left.set_left(LeafNode(10))
    left.set_right(LeafNode(30))
    
    right = BinaryNode(75)
    right.set_left(LeafNode(60))
    right.set_right(LeafNode(80))
    
    root.set_left(left)
    root.set_right(right)
    
    return root


def main():
    """Demonstrate binary tree using Composite pattern"""
    
    print("=" * 80)
    print("COMPOSITE PATTERN - BINARY TREE IMPLEMENTATION")
    print("=" * 80)
    print()
    
    # Example 1: Sample binary tree
    print("EXAMPLE 1: Sample Binary Tree")
    print("-" * 80)
    tree1 = create_sample_tree()
    print(tree1.display())
    print()
    print(f"Height: {tree1.get_height()}")
    print(f"Total Nodes: {tree1.count_nodes()}")
    print(f"Sum of Values: {tree1.sum_values()}")
    print(f"Inorder: {tree1.inorder()}")
    print(f"Preorder: {tree1.preorder()}")
    print(f"Postorder: {tree1.postorder()}")
    print()
    
    # Example 2: Balanced binary tree
    print("=" * 80)
    print("EXAMPLE 2: Balanced Binary Tree")
    print("-" * 80)
    tree2 = create_balanced_tree()
    print(tree2.display())
    print()
    print(f"Height: {tree2.get_height()}")
    print(f"Total Nodes: {tree2.count_nodes()}")
    print(f"Sum of Values: {tree2.sum_values()}")
    print(f"Inorder: {tree2.inorder()}")
    print()
    
    # Example 3: Single node tree
    print("=" * 80)
    print("EXAMPLE 3: Single Node Tree")
    print("-" * 80)
    tree3 = LeafNode(42)
    print(tree3.display())
    print()
    print(f"Height: {tree3.get_height()}")
    print(f"Total Nodes: {tree3.count_nodes()}")
    print(f"Sum of Values: {tree3.sum_values()}")
    print()
    
    # Example 4: Left-skewed tree
    print("=" * 80)
    print("EXAMPLE 4: Left-Skewed Tree")
    print("-" * 80)
    tree4 = BinaryNode(100)
    current = tree4
    for value in [80, 60, 40, 20]:
        left_child = BinaryNode(value)
        current.set_left(left_child)
        current = left_child
    current.set_left(LeafNode(10))
    
    print(tree4.display())
    print()
    print(f"Height: {tree4.get_height()}")
    print(f"Total Nodes: {tree4.count_nodes()}")
    print(f"Sum of Values: {tree4.sum_values()}")
    print()
    
    # Demonstrate Composite Pattern Benefits
    print("=" * 80)
    print("COMPOSITE PATTERN BENEFITS IN BINARY TREES")
    print("=" * 80)
    print("✓ Uniform interface: Both leaves and branches implement TreeNode")
    print("✓ Recursive operations: Methods work on entire subtrees")
    print("✓ Transparent composition: Client treats all nodes uniformly")
    print("✓ Easy extension: Can add new node types easily")
    print("✓ Natural tree structure representation")
    print()
    
    # Show that operations work uniformly on any node
    print("=" * 80)
    print("UNIFORM TREATMENT DEMONSTRATION")
    print("=" * 80)
    
    # Get left subtree of tree1
    left_subtree = tree1.left
    if left_subtree is not None:
        print("Operations on LEFT SUBTREE of tree1:")
        print(left_subtree.display())
        print(f"  Subtree Height: {left_subtree.get_height()}")
        print(f"  Subtree Nodes: {left_subtree.count_nodes()}")
        print(f"  Subtree Sum: {left_subtree.sum_values()}")
        print()
    
    # Get a leaf node
    leaf = tree1.left
    if leaf is not None and isinstance(leaf, BinaryNode):
        leaf = leaf.left
        if leaf is not None and isinstance(leaf, BinaryNode):
            leaf = leaf.left
            if leaf is not None:
                print("Operations on LEAF NODE:")
                print(leaf.display())
                print(f"  Leaf Height: {leaf.get_height()}")
                print(f"  Leaf Nodes: {leaf.count_nodes()}")
                print(f"  Leaf Sum: {leaf.sum_values()}")
                print()
    
    print("=" * 80)
    print("Notice: Same operations work on entire tree, subtree, or single leaf!")
    print("This is the power of the Composite pattern! 🌳")
    print("=" * 80)


if __name__ == "__main__":
    main()