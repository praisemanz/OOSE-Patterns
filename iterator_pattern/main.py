"""
Main program for Iterator Pattern demonstration
Demonstrates custom iterators using Python's built-in iterator interface.
"""

from song import Song
from playlist import Playlist


def main():
    """Demonstrate the Iterator pattern with various iteration strategies"""
    
    print("=" * 70)
    print("ITERATOR PATTERN DEMONSTRATION")
    print("=" * 70)
    print()
    
    # Create a playlist
    my_playlist = Playlist("Road Trip Mix")
    
    # Add songs to the playlist
    my_playlist.add_song(Song("Bohemian Rhapsody", "Queen", 354))
    my_playlist.add_song(Song("Hotel California", "Eagles", 391))
    my_playlist.add_song(Song("Stairway to Heaven", "Led Zeppelin", 482))
    my_playlist.add_song(Song("Sweet Child O' Mine", "Guns N' Roses", 356))
    my_playlist.add_song(Song("Don't Stop Believin'", "Journey", 251))
    my_playlist.add_song(Song("We Will Rock You", "Queen", 122))
    my_playlist.add_song(Song("Another One Bites the Dust", "Queen", 215))
    
    print(f"Playlist: {my_playlist.name}")
    print(f"Total songs: {my_playlist.get_song_count()}")
    print()
    
    # Demonstration 1: Default (Forward) Iterator
    print("-" * 70)
    print("1. FORWARD ITERATION (Default __iter__):")
    print("-" * 70)
    for i, song in enumerate(my_playlist, 1):
        print(f"   {i}. {song}")
    print()
    
    # Demonstration 2: Reverse Iterator
    print("-" * 70)
    print("2. REVERSE ITERATION:")
    print("-" * 70)
    for i, song in enumerate(my_playlist.reverse_iterator(), 1):
        print(f"   {i}. {song}")
    print()
    
    # Demonstration 3: Shuffle Iterator
    print("-" * 70)
    print("3. SHUFFLE ITERATION:")
    print("-" * 70)
    for i, song in enumerate(my_playlist.shuffle_iterator(), 1):
        print(f"   {i}. {song}")
    print()
    
    # Demonstration 4: Filtered Iterator (Queen songs only)
    print("-" * 70)
    print("4. FILTERED ITERATION (Queen songs only):")
    print("-" * 70)
    for i, song in enumerate(my_playlist.filter_by_artist("Queen"), 1):
        print(f"   {i}. {song}")
    print()
    
    # Demonstration 5: Using iterator with list comprehension
    print("-" * 70)
    print("5. USING ITERATOR IN LIST COMPREHENSION:")
    print("-" * 70)
    long_songs = [song.title for song in my_playlist if song.duration > 300]
    print(f"   Songs longer than 5 minutes: {long_songs}")
    print()
    
    # Demonstration 6: Multiple simultaneous iterations
    print("-" * 70)
    print("6. MULTIPLE SIMULTANEOUS ITERATIONS:")
    print("-" * 70)
    print("   Creating two independent iterators:")
    iter1 = iter(my_playlist)
    iter2 = iter(my_playlist)
    
    print(f"   Iterator 1 - First song: {next(iter1).title}")
    print(f"   Iterator 2 - First song: {next(iter2).title}")
    print(f"   Iterator 1 - Second song: {next(iter1).title}")
    print(f"   Iterator 2 - Second song: {next(iter2).title}")
    print()
    
    print("=" * 70)
    print("PATTERN BENEFITS DEMONSTRATED:")
    print("-" * 70)
    print("✓ Built-in Python iterator interface (__iter__ and __next__)")
    print("✓ Multiple iteration strategies without changing collection")
    print("✓ Clean separation between collection and traversal logic")
    print("✓ Support for Python's for-loop syntax and comprehensions")
    print("✓ Independent iterators can traverse the same collection")
    print("✓ Encapsulation: Internal collection structure is hidden")
    print("=" * 70)


if __name__ == "__main__":
    main()
