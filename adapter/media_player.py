"""Target interface that client expects"""
from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, file_name: str) -> None:
        pass
