#Variable-Length Arguments in Python (*args and **kwargs) (VLA)
# In Python, functions can accept a variable number of arguments using:

# *args → Variable-length positional arguments (Tuple)
# **kwargs → Variable-length keyword arguments (Dictionary)

# *args → Variable-length positional arguments
# 1. Using *args (Multiple Positional Arguments)
# ✅ Allows a function to accept any number of positional arguments.
# ✅ Collects them into a tuple.

def profile(*args):
    print(args)
    for i in args:
        print(i)

profile(1,2,3,4,5,'hi','hello')
# (1, 2, 3, 4, 5)

def sum_numbers(*numbers):
    s = sum(numbers)
    print(s)

sum_numbers(10,20)
# 30

sum_numbers(40,50,10,20)
# 120
