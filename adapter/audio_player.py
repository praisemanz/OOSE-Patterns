"""Concrete class implementing MediaPlayer - uses adapter for advanced formats"""
from media_player import MediaPlayer
from media_adapter import MediaAdapter


class AudioPlayer(MediaPlayer):
    def __init__(self):
        self.media_adapter = None
    
    def play(self, audio_type: str, file_name: str) -> None:
        # Built-in support for MP3
        if audio_type.lower() == "mp3":
            print(f"Playing MP3 file: {file_name}")
        # Use adapter for other formats
        elif audio_type.lower() in ["mp4"]:
            print(f"Playing MP4 file: {file_name}")
            # self.media_adapter = MediaAdapter(audio_type)
            # self.media_adapter.play(audio_type, file_name)
        else:
            print(f"Invalid media type: {audio_type} format not supported.")
