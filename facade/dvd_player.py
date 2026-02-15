"""Subsystem class - DVD Player"""


class DVDPlayer:
    def on(self) -> None:
        print("DVD Player: Powering ON")
    
    def off(self) -> None:
        print("DVD Player: Powering OFF")
    
    def play(self, movie: str) -> None:
        print(f"DVD Player: Playing '{movie}'")
    
    def stop(self) -> None:
        print("DVD Player: Stopped")
    
    def eject(self) -> None:
        print("DVD Player: Ejecting disc")
