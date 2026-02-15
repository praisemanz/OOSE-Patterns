"""Subsystem class - Sound System"""


class SoundSystem:
    def on(self) -> None:
        print("Sound System: Powering ON")
    
    def off(self) -> None:
        print("Sound System: Powering OFF")
    
    def set_volume(self, level: int) -> None:
        print(f"Sound System: Setting volume to {level}")
    
    def set_surround_sound(self) -> None:
        print("Sound System: Setting to 5.1 surround sound")
