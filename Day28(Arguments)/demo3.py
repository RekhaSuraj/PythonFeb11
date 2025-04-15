
# Default Arguments
# In a function, arguments can have default values.
# We assign default values to the argument using the ‘=’ (assignment) operator at the time of function definition.
# You can define a function with any number of default arguments.

def profile(name='abc',age=20,salary=60000):
    print('Name',name)
    print('Age',age)
    print('Salary',salary)

# Without passing any arguments
# profile()
# Name abc
# Age 20
# Salary 60000

# Override/replace the default name
# profile('Students')
# Name Students
# Age 20
# Salary 60000

# Replacing all values of default values
profile('Test',10,30000)
# Name Test
# Age 10
# Salary 30000
