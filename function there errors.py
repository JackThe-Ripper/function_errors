import random

def my_function():
    x = random.choice([TypeError, ValueError, RuntimeError])
    raise(x)
try:
    my_function()
except TypeError as a:
    print('it"s Type!', a)
except ValueError as b:
    print('It"s Value!', b)
except RuntimeError as c:
    print('It"s Time!', c)

