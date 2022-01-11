'''
The Facade design pattern provides a solution:
    "Define a separate Facade object that provides an unified interface for a set of interfaces
    in a subsystem. Work through a Facade to minimize dependencies on a subsystem." [GoF]
'''


from abc import ABC, abstractmethod


class SubsystemOne:

    def operation(self):
        print("Subsystem One is working.") 

class SubsystemTwo:

    def operation(self):
        print("Subsystem Two is working.") 


#Before
class ClientBeforeFacade:

    def call_system(self, system1:SubsystemOne, system2:SubsystemTwo):
        system1.operation()
        system2.operation()


#After

class AbstractFacade(ABC):

    @abstractmethod
    def operation(self):
        pass

class FacadeConcrete(AbstractFacade):

    def __init__(self, system1:SubsystemOne, system2:SubsystemTwo) -> None:
        self.__system1 = system1
        self.__system2 = system2
    
    def operation(self):
        self.__system1.operation()
        self.__system2.operation()

class ClientAfterFacade:

    def call_system(self, system:AbstractFacade):
        system.operation()


system_one = SubsystemOne()
system_two = SubsystemTwo()
facade = FacadeConcrete(system_one, system_two)
client = ClientAfterFacade()
client.call_system(facade)
