"""
ForwardIterator - Concrete Iterator for Iterator Pattern
Traverses the playlist from beginning to end.
"""

from typing import List, Iterator
from song import Song


class ForwardIterator:
    """Iterator that traverses the playlist from beginning to end"""
    
    def __init__(self, songs: List[Song]):
        self._songs = songs
        self._index = 0
    
    def __iter__(self) -> Iterator[Song]:
        """Returns the iterator object itself"""
        return self
    
    def __next__(self) -> Song:
        """Returns the next song in forward order"""
        if self._index < len(self._songs):
            song = self._songs[self._index]
            self._index += 1
            return song
        else:
            raise StopIteration
