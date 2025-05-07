# Calling 2 decorators for a single function. Decorator declared just on top of the method will be called first.
# Next the one on top of it.
def upper_fun(definition):
    def inner_fun():
        v1 = definition()
        return v1.upper()

    return inner_fun


def split_fun(name):
    def inner_fun():
        v1 = name()
        return v1.split()

    return inner_fun


@split_fun
@upper_fun
def definition():
    return 'Python is a high level programming language'


@split_fun
@upper_fun
def quote():
    return 'Today is a good day'


print(definition())

# If we apply @split_fun decorator first, then it will throw below error as upper() is a method of string.
# AttributeError: 'list' object has no attribute 'upper'

# ['PYTHON', 'IS', 'A', 'HIGH', 'LEVEL', 'PROGRAMMING', 'LANGUAGE']


print(quote())
# ['TODAY', 'IS', 'A', 'GOOD', 'DAY']