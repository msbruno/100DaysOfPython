class AccountService:

    def __init__(self, registration_function) -> None:
        self.__registration_function = registration_function

    def register(self, name:str):
        result = self.__registration_function(name)
        #logic
        return result

'''
    STUB
    
    Definition:
    "Stub - a dumb piec of software that simply replies the same way every time.
    -- Dave Farley

    Problems:
    They are pretty simple and don't usually cause too much problem.
    Except people sometimes don't think of using them when they should.

'''
def _stub_accept_registration(name):
    return True
    
def _stub_reject_registration(name):
    return False

class RegistrationTestCase(unittest.TestCase):

    def test_should_accept_registration(self):
        sut = AccountService(_stub_accept_registration)
        self.assertTrue(sut.register("name"))
    
    def test_should_reject_registration(self):
        sut = AccountService(_stub_reject_registration)
        self.assertFalse(sut.register("name"))


''' 
    FAKE

    Definition:
    "A stub is done, it will return the same value every time   
    A Fake is a little smarter, it has some behavior coded into."
    -- Dave Farley

    Problem:
    Peolple try to make fakes horribly complex.
    Specially when they are trying some simulation and imagine simulators nearly complex as the original system.
'''
def _fake_registration_function(name):
    return name == "Bruno"


class RegistrationTestCase(unittest.TestCase):

    def test_should_accept_registration(self):
        sut = AccountService(_fake_registration_function)
        self.assertTrue(sut.register("Bruno"))
    
    def test_should_reject_registration(self):
        sut = AccountService(_fake_registration_function)
        self.assertFalse(sut.register("other_name"))
