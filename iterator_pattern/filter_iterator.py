"""
FilterIterator - Concrete Iterator for Iterator Pattern
Traverses only songs matching a filter condition.
"""

from typing import List, Iterator, Callable
from song import Song


class FilterIterator:
    """Iterator that only returns songs matching a filter condition"""
    
    def __init__(self, songs: List[Song], filter_func: Callable[[Song], bool]):
        self._songs = [song for song in songs if filter_func(song)]
        self._index = 0
    
    def __iter__(self) -> Iterator[Song]:
        """Returns the iterator object itself"""
        return self
    
    def __next__(self) -> Song:
        """Returns the next song matching the filter"""
        if self._index < len(self._songs):
            song = self._songs[self._index]
            self._index += 1
            return song
        else:
            raise StopIteration
