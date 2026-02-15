"""Concrete implementation of AdvancedMediaPlayer for VLC"""
from advanced_media_player import AdvancedMediaPlayer


class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, file_name: str) -> None:
        print(f"Playing VLC file: {file_name}")
    
    def play_mp4(self, file_name: str) -> None:
        # Do nothing - VlcPlayer doesn't support MP4
        pass
