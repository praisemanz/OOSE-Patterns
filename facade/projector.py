"""Subsystem class - Projector"""


class Projector:
    def on(self) -> None:
        print("Projector: Powering ON")
    
    def off(self) -> None:
        print("Projector: Powering OFF")
    
    def wide_screen_mode(self) -> None:
        print("Projector: Setting to widescreen mode (16:9)")
    
    def set_input(self, input_source: str) -> None:
        print(f"Projector: Setting input to {input_source}")
