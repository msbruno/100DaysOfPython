from abc import ABC, abstractmethod
'''
Composite Intent:
    "Compose objects into tree structures to represent part-whole hierarchies. Composite lets
    clients treat individual objects and compositions of objects uniformly." [GoF]
'''

class Component(ABC):

    @abstractmethod
    def do_operation(self):
        pass

class Leaf(Component):

    def __init__(self, id:int): 
        self.__id = id

    def do_operation(self):
        print("Leaf {}".format(self.__id))

class Composite(Component):

    def __init__(self, id:int) -> None:
        self.__children:list[Component] = []
        self.__id = id

    def add(self, component):
        self.__children.append(component)
    
    def do_operation(self):
        print("Composite {}".format(self.__id))
        for child in self.__children:
            child.do_operation()


first_composite = Composite(1)
first_composite.add(Leaf(1))
first_composite.add(Leaf(2))
first_composite.add(Leaf(3))

second_composite = Composite(2)
second_composite.add(Leaf(4))
second_composite.add(Leaf(5))
second_composite.add(first_composite)

second_composite.do_operation()
