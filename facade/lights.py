"""Subsystem class - Lights"""


class Lights:
    def dim(self, level: int) -> None:
        print(f"Lights: Dimming to {level}%")
    
    def on(self) -> None:
        print("Lights: Turning ON to full brightness")
