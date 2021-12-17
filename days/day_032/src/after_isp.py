# AFTER IMPLEMENTING INTERFACE SEGREGATION PRINCIPLE
class CalculateArea:

    def area(self):
        raise Exception("Method Not Implemented.")

class CalculatePerimeter:
    def perimeter(self):
        raise Exception("Method Not Implemented.")

class Square(CalculateArea, CalculatePerimeter):

    def __init__(self, size:int) -> None:
        self.__size = size

    def area(self):
        return self.__size ** 2
    
    def perimeter(self):
        return self.__size * 4

assert Square(2).area() == 4
assert Square(2).perimeter() == 8
