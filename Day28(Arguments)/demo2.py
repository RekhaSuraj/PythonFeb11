
# Keyword Arguments
# Arguments are passed by parameter names, so order does not matter.

def function_hello(name,age):
    print('Name',name)
    print('Age',age)

function_hello(age=11,name='Test')


def function_sum(n1,n2,n3):
    print(n1+n2+n3)

function_sum(5,10,25)

# First we have to pass positional arguments, and then keyword arguments
# Mixing positional and keyword arguments
def info(name,age,salary):
    print('Name',name)
    print('Age',age)
    print('Salary',salary)

# info(age=20, name='Test',50000)
# SyntaxError: positional argument follows keyword argument

info('Test',salary=5000,age=20)
