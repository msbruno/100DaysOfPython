'''
    SPY / Mock
    Definition:
    " A way to figure out what happened. We can use some code to record what happens while it's happening
    and then afterwards it allows us to query it and make assertions on whatever it is that we find."

    Problems:
    - "People end up writing up test using mocks that are so complex that there are actually no real code
    being tested, it's all mocks. If you find your selff ever returning a mock from a mock, I recomend that you
    stop and think about your design for a moment."
    - "If you find yourself writing code to simulate some behavior in a mock -  and I know library mocks let you do 
    this - but should? should you really?"
    - "If you find yourself validating that your code calls some dependency 17x, with one set of parameters and three more with
    another, then you have a problem - and it's not the mock's fault. 
'''
class RegistrationTestCase(unittest.TestCase):

    '''
        In this example we are interested in whether the core was made correctly or not.
    '''
    def test_should_accept_registration(self):
        sut = AccountService(self._spy_registration_function)
        self.assertTrue(sut.register("Bruno"))
        self.assertEqual("Bruno", self.name)
    
    def _spy_registration_function(self, name):
        self.name = name
        return True
