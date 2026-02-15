"""
ShuffleIterator - Concrete Iterator for Iterator Pattern
Traverses the playlist in random order.
"""

from typing import List, Iterator
import random
from song import Song


class ShuffleIterator:
    """Iterator that traverses the playlist in random order"""
    
    def __init__(self, songs: List[Song]):
        self._songs = songs.copy()  # Don't modify original
        random.shuffle(self._songs)
        self._index = 0
    
    def __iter__(self) -> Iterator[Song]:
        """Returns the iterator object itself"""
        return self
    
    def __next__(self) -> Song:
        """Returns the next song in shuffled order"""
        if self._index < len(self._songs):
            song = self._songs[self._index]
            self._index += 1
            return song
        else:
            raise StopIteration
