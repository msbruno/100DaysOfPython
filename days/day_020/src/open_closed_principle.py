'''
Evolving the code from Single Responsability Principle, adding Open closed Principle.
First code: https://github.com/msbruno/100DaysOfPython/blob/main/days/day_019/single_resposability_principle.py
'''

from abc import ABC, abstractmethod
from functools import reduce

class Item:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self) -> str:
        return f'item -> {self.__name}, price-> {self.__price}'

    def price(self):
        return self.__price

class OrderSRP:
    def __init__(self) -> None:
        self.__itens:list = []
        self.status = 'unpaid'

    def total_price(self):
        return reduce((lambda x,y: x.price() + y.price()), self.__itens)


    def add_item(self, item):
        self.__itens.append(item)

    def __str__(self) -> str:
        result = ''
        for item in self.__itens:
            result += str(item)
        return result

class PaymentProcessor(ABC):
  '''Adding open closed principle'''

    @abstractmethod
    def pay(self, order):
        pass
    
class PaymentDebitProcessor(PaymentProcessor):

    def pay(self, order)-> Order:
        print("Processing using debit type")
        print(order)
        order.status = "paid"
        return order

class PaymentCreditProcessor(PaymentProcessor):

    def pay(self, order)-> Order:
        print("Processing using credit type")
        print(order)
        order.status = "paid"
        return order

order = OrderSRP()
order.add_item(Item("Valid-Item-1", 1.5))
order.add_item(Item("Valid-Item-2", 2.5))

debit_processor = PaymentDebitProcessor()
result = debit_processor.pay(order)
assert 4.0 == result.total_price() 
assert 'paid' == result.status 


