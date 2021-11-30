class Item:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self) -> str:
        return f'item -> {self.__name}, price-> {self.__price}'

    def price(self):
        return self.__price

from functools import reduce

class Order:
  
  ''' Order is not following Single responsability principle. '''

    def __init__(self):
        self.__itens:list = []
        self.status = 'unpaid'

    def total_price(self):
        return sum(self.__itens)

    def add_item(self, item):
        self.__itens.append(item)

    def process_order(self, payment:str):
        if payment == 'credit':
            print('processing credit payment - total: ${}'.format(self.total_price()))
            self.status = 'paid'
        elif payment == 'debit':
            print('processing credit payment - total: ${}'.format(self.total_price()))
            self.status = 'paid'

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

class PaymentProcessor():

    def pay(self, order, payment):
        if payment == 'credit':
            print('processing credit payment - total: ${}'.format(order.total_price()))
            order.status = 'paid'
        elif payment == 'debit':
            print('processing credit payment - total: ${}'.format(order.total_price()))
            order.status = 'paid'
        return order

order = OrderSRP()
order.add_item(Item("Valid-Item-1", 1.5))
order.add_item(Item("Valid-Item-2", 2.5))

debit_processor = PaymentProcessor()
result = debit_processor.pay(order, "debit")
assert 4.0 == result.total_price() 
assert 'paid' == result.status 
