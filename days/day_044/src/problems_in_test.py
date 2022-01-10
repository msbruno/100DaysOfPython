'''
Mistakes in Tests
source: https://www.youtube.com/watch?v=W40mpZP9xQQ
'''
import unittest

class Calculator:

    def __init__(self) -> None:
        self.__list = list()

    def percentage(self, percentage:float, number:int):
        return percentage * number

    def add_to_list(self, number:int):
        self.__list.append(number)

    def sum_list(self)->int:
        return sum(self.__list)


class PercentageTestCase(unittest.TestCase):

    def test_should_return_percentage(self):
        self.assertEqual(10, Calculator().percentage(10,100))

    def test_mistake_repeated_test_with_different_inputs(self):
        '''
            "The time for testing for different input is when either the new test demands 
            new behavior - so changing our implementation - or when we are not quite sure of the result, for some reason.
            -- Dave Farley
        '''
        self.assertEqual(5, Calculator().percentage(5,100))


    def test_mistake_duplicate_logic(self):
        '''"Your test is simply saying "the code I wrote is the code I wrote
            Make your assertion definitive and distinct from the code you're testing."
            -- Dave Farley
        '''
        self.assertEqual(5*100, Calculator().percentage(5,100))
    
    def test_mistake_iterate_through_test(self):
        sut = Calculator()

        #"TTD expert John Jagger says that cyclomathic complex of a test should be 1."
        for i in range(5):
            sut.add_to_list(i)
        self.assertEqual(10, sut.sum_list())
