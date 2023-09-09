"""_
    Dependency Inversion Principle (DIP):
This principle states that high-level modules should not depend on low-level modules; both should depend on abstractions. In Python, 
you can use dependency injection and abstractions (e.g., interfaces or abstract base classes) to achieve this.summary_
"""


from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Light bulb is on")

    def turn_off(self):
        print("Light bulb is off")

class Fan(Switchable):
    def turn_on(self):
        print("Fan is on")

    def turn_off(self):
        print("Fan is off")

class ElectricPowerSwitch:
    def __init__(self, device):
        self.device = device
        self.on = False

    def press(self):
        if self.on:
            self.device.turn_off()
            self.on = False
        else:
            self.device.turn_on()
            self.on = True
