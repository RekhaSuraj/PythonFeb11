import sys
# Recursive function has 3 components:
# 1. Function Definition
# 2. Base case (Exit condition)
# 3. Recursive case

# set a recursion limit
sys.setrecursionlimit(100)

def call():
    print('hello')
    call()
call()

# [Previous line repeated 96 more times]
# RecursionError: maximum recursion depth exceeded