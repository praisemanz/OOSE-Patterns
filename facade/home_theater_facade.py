"""Facade class - provides simplified interface to complex subsystems"""
from dvd_player import DVDPlayer
from projector import Projector
from sound_system import SoundSystem
from lights import Lights


class HomeTheaterFacade:
    def __init__(self, dvd: DVDPlayer, proj: Projector, 
                 sound: SoundSystem, lights: Lights):
        self.dvd_player = dvd
        self.projector = proj
        self.sound_system = sound
        self.lights = lights
    
    def watch_movie(self, movie: str) -> None:
        """Simplified method to watch a movie"""
        print("\n*** Get ready to watch a movie... ***\n")
        self.lights.dim(10)
        self.projector.on()
        self.projector.wide_screen_mode()
        self.projector.set_input("DVD")
        self.sound_system.on()
        self.sound_system.set_surround_sound()
        self.sound_system.set_volume(15)
        self.dvd_player.on()
        self.dvd_player.play(movie)
        print("\n*** Movie is now playing! Enjoy! ***\n")
    
    def end_movie(self) -> None:
        """Simplified method to end movie"""
        print("\n*** Shutting down home theater... ***\n")
        self.dvd_player.stop()
        self.dvd_player.eject()
        self.dvd_player.off()
        self.sound_system.off()
        self.projector.off()
        self.lights.on()
        print("\n*** Home theater is OFF ***\n")
