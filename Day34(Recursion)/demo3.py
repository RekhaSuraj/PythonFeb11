import demo2
# Import only specific classes or functions from a module
from demo1 import addition
from demo1 import subtraction

# This will import all functions present in demo1
from demo1 import *

# calling demo1 module
# print(demo1.addition(int(input('Enter first number')),int(input('Enter second number'))))

# Direct calling the function when we give "from demo1 import *" or "from demo1 import <function_name>
print(addition(10,20))
# Enter first number8
# Enter second number5
# Addition of 8 and 5 is 13

print(subtraction(10,5))
# Subtraction of 10 and 5 is 5

# Calling demo2 module as we have directly given "import demo2"
print(demo2.cube_n(int(input('Enter a number'))))
# Enter a number4
# 64

print(demo2.power(5,6))
# 15625