from dataclasses import dataclass
from datetime import date

""" this annotation provides a decorator for automatically adding generated methods like __init__() 
to user defined methods """
@dataclass
class Person:

    """ Class to represent a person. """ 
    name: str
    surname: str
    birth_date: date = date.today()

def test():
    name = "valid_name"
    surname = "valid_surname"
    today = date.today()

    #
    person = Person(name=name, surname=surname, birth_date=today)
    assert person.name == name
    assert person.surname == surname
    assert person.birth_date == today

    #
    person = Person(name, surname)
    assert person.name == name
    assert person.surname == surname
    assert person.birth_date == today


test()



