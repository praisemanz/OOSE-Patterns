"""
ReverseIterator - Concrete Iterator for Iterator Pattern
Traverses the playlist from end to beginning.
"""

from typing import List, Iterator
from song import Song


class ReverseIterator:
    """Iterator that traverses the playlist from end to beginning"""
    
    def __init__(self, songs: List[Song]):
        self._songs = songs
        self._index = len(songs) - 1
    
    def __iter__(self) -> Iterator[Song]:
        """Returns the iterator object itself"""
        return self
    
    def __next__(self) -> Song:
        """Returns the next song in reverse order"""
        if self._index >= 0:
            song = self._songs[self._index]
            self._index -= 1
            return song
        else:
            raise StopIteration
