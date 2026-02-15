"""
Song - Data class for Iterator Pattern
Represents a song with title, artist, and duration.
"""

from dataclasses import dataclass


@dataclass
class Song:
    """Represents a song with title, artist, and duration"""
    title: str
    artist: str
    duration: int  # in seconds
    
    def __str__(self) -> str:
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f'"{self.title}" by {self.artist} ({minutes}:{seconds:02d})'
