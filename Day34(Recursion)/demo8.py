# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept.
# It means that a function calls itself.
# This has the benefit of meaning that you can loop through data to reach a result.
import sys
# def Call():
#     print('hello function')
#     Call()
# Call()

# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# reason for display upto 996---the main problem is stack overflow and the memory utiliztion
# -------------------------------------------------------------------------------------------------
#  the maximum recursion depth that Python can handle depends on the available memory
# and the size of the call stack. In some cases, the recursion limit of 1000 may be
# reached before the call stack is full, resulting in a stack overflow error.
#
# In your specific case, the recursion limit of 1000 was reached before the call stack
# was completely filled, allowing Python to display up to 996 iterations. The exact
# number of iterations that can be displayed may depending on the factors mentioned above.


print(sys.getrecursionlimit())
# 1000