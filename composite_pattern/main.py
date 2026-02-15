"""
Main program for Composite Pattern demonstration
Demonstrates a file system structure with files and directories.
"""

from file import File
from directory import Directory


def main():
    """Demonstrate the Composite pattern with a file system structure"""
    
    print("=" * 60)
    print("COMPOSITE PATTERN DEMONSTRATION")
    print("=" * 60)
    print()
    
    # Create the root directory
    root = Directory("root")
    
    # Create documents directory with files
    documents = Directory("documents")
    documents.add(File("resume.pdf", 150))
    documents.add(File("cover_letter.docx", 45))
    
    # Create projects directory
    projects = Directory("projects")
    
    # Create a nested project directory
    project1 = Directory("website_redesign")
    project1.add(File("index.html", 12))
    project1.add(File("styles.css", 8))
    project1.add(File("script.js", 15))
    
    # Create images subdirectory within project
    images = Directory("images")
    images.add(File("logo.png", 85))
    images.add(File("banner.jpg", 120))
    project1.add(images)
    
    # Add project1 to projects
    projects.add(project1)
    
    # Create another project
    project2 = Directory("mobile_app")
    project2.add(File("main.java", 45))
    project2.add(File("config.xml", 5))
    projects.add(project2)
    
    # Create media directory
    media = Directory("media")
    
    # Create music subdirectory
    music = Directory("music")
    music.add(File("song1.mp3", 4500))
    music.add(File("song2.mp3", 3800))
    media.add(music)
    
    # Create videos subdirectory
    videos = Directory("videos")
    videos.add(File("tutorial.mp4", 15000))
    media.add(videos)
    
    # Build the complete tree
    root.add(documents)
    root.add(projects)
    root.add(media)
    root.add(File("readme.txt", 2))
    
    # Display the entire tree structure
    print("FILE SYSTEM TREE STRUCTURE:")
    print("-" * 60)
    root.display()
    
    print()
    print("=" * 60)
    print("SIZE CALCULATIONS:")
    print("-" * 60)
    
    # Demonstrate uniform treatment of leaf and composite objects
    print(f"Total size of root: {root.get_size()} KB")
    print(f"Size of documents folder: {documents.get_size()} KB")
    print(f"Size of website_redesign project: {project1.get_size()} KB")
    print(f"Size of resume.pdf file: {documents.get_child(0).get_size()} KB")
    print(f"Size of media folder: {media.get_size()} KB")
    
    print()
    print("=" * 60)
    print("PATTERN BENEFITS DEMONSTRATED:")
    print("-" * 60)
    print("✓ Uniform treatment: Both files and directories use get_size()")
    print("✓ Tree structure: Nested directories create hierarchy")
    print("✓ Recursive operations: display() works on entire tree")
    print("✓ Flexibility: Easy to add new files/directories anywhere")
    print("=" * 60)


if __name__ == "__main__":
    main()
