"""Concrete implementation of AdvancedMediaPlayer for MP4"""
from advanced_media_player import AdvancedMediaPlayer


class Mp4Player(AdvancedMediaPlayer):
    def play_vlc(self, file_name: str) -> None:
        # Do nothing - Mp4Player doesn't support VLC
        pass
    
    def play_mp4(self, file_name: str) -> None:
        print(f"Playing MP4 file: {file_name}")
