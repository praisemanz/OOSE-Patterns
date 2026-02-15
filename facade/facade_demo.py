"""Main class demonstrating the Facade pattern"""
import time
from dvd_player import DVDPlayer
from projector import Projector
from sound_system import SoundSystem
from lights import Lights
from home_theater_facade import HomeTheaterFacade


def main():
    print("=== Facade Pattern Demo - Home Theater System ===")
    
    # Create subsystem components
    dvd = DVDPlayer()
    projector = Projector()
    sound_system = SoundSystem()
    lights = Lights()
    
    # Create facade
    home_theater = HomeTheaterFacade(dvd, projector, sound_system, lights)
    
    # Use simplified interface
    home_theater.watch_movie("The Matrix")
    
    # Simulate some time passing
    time.sleep(2)
    
    home_theater.end_movie()
    
    print("=== Demo Complete ===")


if __name__ == "__main__":
    main()
