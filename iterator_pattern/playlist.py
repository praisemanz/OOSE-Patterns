"""
Playlist - Aggregate class for Iterator Pattern
A playlist collection that supports multiple iteration strategies.
"""

from typing import List, Iterator
from song import Song
from forward_iterator import ForwardIterator
from reverse_iterator import ReverseIterator
from shuffle_iterator import ShuffleIterator
from filter_iterator import FilterIterator


class Playlist:
    """
    A playlist collection that supports multiple iteration strategies.
    Implements the built-in Python iterator protocol via __iter__.
    """
    
    def __init__(self, name: str):
        self.name = name
        self._songs: List[Song] = []
    
    def add_song(self, song: Song) -> None:
        """Add a song to the playlist"""
        self._songs.append(song)
    
    def remove_song(self, song: Song) -> None:
        """Remove a song from the playlist"""
        self._songs.remove(song)
    
    def get_song_count(self) -> int:
        """Get the number of songs in the playlist"""
        return len(self._songs)
    
    # Default iterator: Forward iteration
    def __iter__(self) -> Iterator[Song]:
        """
        Returns the default iterator (forward).
        This is the built-in Python iterator interface.
        """
        return ForwardIterator(self._songs)
    
    # Alternative iteration strategies
    def reverse_iterator(self) -> Iterator[Song]:
        """Returns an iterator that traverses songs in reverse order"""
        return ReverseIterator(self._songs)
    
    def shuffle_iterator(self) -> Iterator[Song]:
        """Returns an iterator that traverses songs in random order"""
        return ShuffleIterator(self._songs)
    
    def filter_by_artist(self, artist: str) -> Iterator[Song]:
        """Returns an iterator for songs by a specific artist"""
        return FilterIterator(self._songs, lambda song: song.artist == artist)
