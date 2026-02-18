"""
Visual Tree Generator for Composite Pattern
Creates an actual tree diagram (like binary tree visualization)
"""

from file_system_component import FileSystemComponent
from file import File
from directory import Directory


class TreeVisualizer:
    """Generates visual tree representations of the file system"""
    
    @staticmethod
    def draw_tree(component: FileSystemComponent, prefix: str = "", is_last: bool = True) -> str:
        """
        Draw a visual tree using box-drawing characters
        
        Uses Unicode box-drawing characters:
        ├── for intermediate nodes
        └── for last nodes
        │   for vertical lines
        """
        result = []
        
        # Determine the connector
        if prefix == "":
            connector = ""
        else:
            connector = "└── " if is_last else "├── "
        
        # Add current node
        if isinstance(component, File):
            result.append(f"{prefix}{connector}📄 {component.name} ({component.get_size()} KB)")
        elif isinstance(component, Directory):
            result.append(f"{prefix}{connector}📁 {component.name}/")
            
            # Add children
            if hasattr(component, 'children') and component.children:
                # Calculate new prefix for children
                if prefix == "":
                    new_prefix = ""
                else:
                    new_prefix = prefix + ("    " if is_last else "│   ")
                
                # Draw all children
                for i, child in enumerate(component.children):
                    is_last_child = (i == len(component.children) - 1)
                    child_lines = TreeVisualizer.draw_tree(child, new_prefix, is_last_child)
                    result.append(child_lines)
        
        return "\n".join(result) if prefix == "" else "".join(result)
    
    @staticmethod
    def draw_ascii_tree(component: FileSystemComponent, prefix: str = "", is_last: bool = True) -> str:
        """
        Draw a visual tree using only ASCII characters (for better compatibility)
        """
        result = []
        
        # Determine the connector
        if prefix == "":
            connector = ""
        else:
            connector = "+-- " if is_last else "|-- "
        
        # Add current node
        if isinstance(component, File):
            result.append(f"{prefix}{connector}[F] {component.name} ({component.get_size()} KB)")
        elif isinstance(component, Directory):
            result.append(f"{prefix}{connector}[D] {component.name}/")
            
            # Add children
            if hasattr(component, 'children') and component.children:
                # Calculate new prefix for children
                if prefix == "":
                    new_prefix = ""
                else:
                    new_prefix = prefix + ("    " if is_last else "|   ")
                
                # Draw all children
                for i, child in enumerate(component.children):
                    is_last_child = (i == len(component.children) - 1)
                    child_lines = TreeVisualizer.draw_ascii_tree(child, new_prefix, is_last_child)
                    result.append(child_lines)
        
        return "\n".join(result) if prefix == "" else "".join(result)
    
    @staticmethod
    def draw_graphical_tree(component: FileSystemComponent, level: int = 0, is_last: bool = True, 
                          parent_prefix: str = "") -> str:
        """
        Draw a more graphical tree similar to binary tree visualizations
        """
        result = []
        
        # Create the connection lines
        if level == 0:
            prefix = ""
            connector = ""
            new_parent_prefix = ""
        else:
            if is_last:
                connector = "    └── "
                new_parent_prefix = parent_prefix + "        "
            else:
                connector = "    ├── "
                new_parent_prefix = parent_prefix + "    │   "
            prefix = parent_prefix
        
        # Add current node
        if isinstance(component, File):
            node_repr = f"📄 {component.name} ({component.get_size()} KB)"
        else:
            node_repr = f"📁 {component.name}/ (Total: {component.get_size()} KB)"
        
        result.append(f"{prefix}{connector}{node_repr}")
        
        # Add children for directories
        if isinstance(component, Directory) and component.children:
            for i, child in enumerate(component.children):
                is_last_child = (i == len(component.children) - 1)
                child_tree = TreeVisualizer.draw_graphical_tree(
                    child, level + 1, is_last_child, new_parent_prefix
                )
                result.append(child_tree)
        
        return "\n".join(result)


def main():
    """Demonstrate visual tree generation for Composite pattern"""
    
    print("=" * 80)
    print("COMPOSITE PATTERN - VISUAL TREE REPRESENTATIONS")
    
    # Create the same file system structure
    root = Directory("root")
    
    # Documents directory
    documents = Directory("documents")
    documents.add(File("resume.pdf", 150))
    documents.add(File("cover_letter.docx", 45))
    documents.add(File("references.txt", 10))
    
    # Projects directory
    projects = Directory("projects")
    
    # Website project
    website = Directory("website_redesign")
    website.add(File("index.html", 12))
    website.add(File("styles.css", 8))
    website.add(File("script.js", 15))
    
    # Images subdirectory
    images = Directory("images")
    images.add(File("logo.png", 85))
    images.add(File("banner.jpg", 120))
    images.add(File("favicon.ico", 2))
    website.add(images)
    
    projects.add(website)
    
    # Mobile app project
    mobile = Directory("mobile_app")
    mobile.add(File("main.java", 45))
    mobile.add(File("config.xml", 5))
    mobile.add(File("README.md", 8))
    projects.add(mobile)
    
    # Media directory
    media = Directory("media")
    
    # Music
    music = Directory("music")
    music.add(File("song1.mp3", 4500))
    music.add(File("song2.mp3", 3800))
    music.add(File("playlist.m3u", 1))
    media.add(music)
    
    # Videos
    videos = Directory("videos")
    videos.add(File("tutorial.mp4", 15000))
    videos.add(File("demo.avi", 8500))
    media.add(videos)
    
    # Build the tree
    root.add(documents)
    root.add(projects)
    root.add(media)
    root.add(File("readme.txt", 2))
    root.add(File("license.txt", 5))
    

   
  
    print()
    
    #  Graphical Tree with Sizes
    print("=" * 80)
    print("Graphical Tree with Total Sizes")
    print("=" * 80)
    tree3 = TreeVisualizer.draw_graphical_tree(root)
    print(tree3)
    print()
    
    # Summary
    print("=" * 80)
    print("TREE STATISTICS")
    print("=" * 80)
    print(f"Total Size: {root.get_size()} KB")
    print(f"Root has {len(root.children)} direct children")
    print()
    
    # Show the hierarchical structure
    def count_nodes(component):
        if isinstance(component, File):
            return 1, 0  # 1 file, 0 directories
        else:
            files = 0
            dirs = 1  # Count this directory
            for child in component.children:
                f, d = count_nodes(child)
                files += f
                dirs += d
            return files, dirs
    
    total_files, total_dirs = count_nodes(root)
    print(f"Total Files: {total_files}")
    print(f"Total Directories: {total_dirs}")
    print(f"Total Nodes: {total_files + total_dirs}")
    print()
    
    print("=" * 80)
    print("COMPOSITE PATTERN BENEFITS")
    print("=" * 80)
    print("✓ Tree structure clearly visualized")
    print("✓ Parent-child relationships shown")
    print("✓ Hierarchical organization displayed")
    print("✓ Uniform treatment of files and directories")
    print("✓ Easy to add new nodes at any level")
    print("=" * 80)


if __name__ == "__main__":
    main()