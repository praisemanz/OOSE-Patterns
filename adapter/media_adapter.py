"""Adapter class - adapts AdvancedMediaPlayer to MediaPlayer interface"""
from media_player import MediaPlayer
from vlc_player import VlcPlayer
from mp4_player import Mp4Player


class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type: str):
        self.advanced_media_player = None
        
        if audio_type.lower() == "vlc":
            self.advanced_media_player = VlcPlayer()
        elif audio_type.lower() == "mp4":
            self.advanced_media_player = Mp4Player()
    
    def play(self, audio_type: str, file_name: str) -> None:
        if audio_type.lower() == "vlc":
            self.advanced_media_player.play_vlc(file_name) # type: ignore
        elif audio_type.lower() == "mp4":
            self.advanced_media_player.play_mp4(file_name) # type: ignore
