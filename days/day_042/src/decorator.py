'''
The intent of the Decorator:
    "Attach additional responsibilities to an object dynamically. Decorators provide a flexible
    alternative to subclassing for extending functionality." [GoF]

'''

from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def do_operation(self)->str:
        pass

class ConcreteComponent(Component):

    def do_operation(self)->str:
        return "ABCDEFGHIJ"

class Decorator(Component):

    def __init__(self, component:Component):
        self.__component = component

    @abstractmethod
    def add_behavior(self, string:str):
        pass

    def do_operation(self)->str:
        result = self.__component.do_operation()
        return self.add_behavior(result)

class FirstConcreteDecorator(Decorator):

    def add_behavior(self, string: str):
        print('Adding behavior first concrete decorator.')
        result = '#'.join(string)
        print(result)
        return result

class SecondConcreteDecorator(Decorator):

    def add_behavior(self, string: str):
        print('Adding behavior second concrete decorator.')
        result = string.replace('#', '-')
        print(result)
        return result


concrete_component = ConcreteComponent()
first_decorator = FirstConcreteDecorator(concrete_component)
second_decorator = SecondConcreteDecorator(first_decorator)
second_decorator.do_operation()
