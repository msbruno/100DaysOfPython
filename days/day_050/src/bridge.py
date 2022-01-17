"""
The intent of the Bridge design pattern is to:
    "Decouple an abstraction from its implementation
    so that the two can vary independently." [GoF]
"""

from abc import ABC, abstractmethod


class TelevisionGeneric:

    def __init__(self, remote_control):
        self.remote_control = remote_control

    def operation(self)->str:
        print("running a Generic Television.")
        return self.remote_control.operation()

class TelevisionSamsung(TelevisionGeneric):

    def operation(self) -> str:
        print("running a Samsgung Television.")
        return self.remote_control.operation()

class RemoteControl(ABC):

    @abstractmethod
    def operation(self)->str:
        pass

class RemoteControlWithoutBattery(RemoteControl):

    def operation(self) -> str:
        return "Remote Controle implemented without battery"

class RemoteControlWitBattery(RemoteControl):

    def operation(self) -> str:
        return "Remote Controle implemented with battery"

tv = TelevisionSamsung(RemoteControlWitBattery())
print(tv.operation())
# running a Samsgung Television.
# Remote Controle implemented with battery

tv = TelevisionSamsung(RemoteControlWithoutBattery())
print(tv.operation())
# running a Samsgung Television.
# Remote Controle implemented without battery

tv = TelevisionGeneric(RemoteControlWitBattery())
print(tv.operation())
# running a Generic Television.
# Remote Controle implemented with battery

tv = TelevisionGeneric(RemoteControlWithoutBattery())
print(tv.operation())
# running a Generic Television.
# Remote Controle implemented without battery
