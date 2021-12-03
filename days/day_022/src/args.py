# *args allow a function to take any number of positional arguments
def addition(*args):
   result = 0
   for i in args:
      result += i
   return result
   
assert 5 == addition(1,4)
assert 11 == addition(1,7,3)

# each undefined parameter is stored as a key-value pair in kwargs
def arg_dict(a, b, option=True, **kwargs):
   return kwargs

assert {'param1': 10, 'param2': 11} == arg_dict(3, 4, param1=10, param2=11)
