# Types of Arguments :
# 1.Positional Arguments
# 2.Keyword Arguments
# 3.Default Arguments
# 4.Variable Length Arguments

# Positional Arguments:
# Positional arguments are those arguments where values get assigned to the arguments by their position when the function is called.
# For example, the 1st positional argument must be 1st when the function is called.
# The 2nd positional argument needs to be 2nd when the function is called, etc

def profile(name,age,salary):
    print('Name',name)
    print('age',age)
    print('salary',salary)


profile('GRK',25,40000)
# profile(25,40000,'GRK')
# GRK 25 40000

def greetings(name):
    return f'hello {name}'

print(greetings('Students'))
# hello Students

