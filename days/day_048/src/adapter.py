'''
Adapter Design pattern:
    Intent: "Convert the interface of a class into another interface clients expect. Adapter lets classes
    work together that couldn't otherwise because of incompatible interfaces. " [GoF]
'''

from abc import ABC, abstractmethod
from dataclasses import dataclass


class SubmersibleObject(ABC):

    @abstractmethod
    def dive(self)->str:
        pass

class Sea: 

    def submerge_an_object(self, obj:SubmersibleObject):
        print(obj.dive())

# A human can't dive
@dataclass
class Human:
    name:str

# Adapter is an adapter to allow a Human to dive.
class Submarine(SubmersibleObject):

    def __init__(self, human:Human):
        self.__human = human

    def dive(self)->str:
        return "{} is submerged.".format(self.__human.name)

human = Human("Bruno")
submarine = Submarine(human)
sea = Sea()
sea.submerge_an_object(submarine)
#Bruno is submerged.
