"""Main class demonstrating the Adapter pattern"""
from audio_player import AudioPlayer


def main():
    print("=== Adapter Pattern Demo - Media Player ===\n")
    
    audio_player = AudioPlayer()
    
    # Playing different media types
    audio_player.play("mp3", "song.mp3")
    audio_player.play("mp4", "video.mp4")
    audio_player.play("vlc", "movie.vlc")
    audio_player.play("avi", "clip.avi")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
