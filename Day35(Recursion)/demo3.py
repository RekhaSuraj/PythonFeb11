# Factorial of a number using recursion
def factorial_fun(num): # Function definition
    if num == 0: #Exit case
        return 1
    else:
        return num * factorial_fun(num-1) # Recursuive case

print(factorial_fun(5))

# =5*factorial_fun(4)
# =5*4*factorial_fun(3)
# =5*4*3*factorial_fun(2)
# =5*4*3*2*factorial_fun(1)
# =5*4*3*2*1*factorial_fun(0)
# =5*4*3*2*1*1
# =120

# hw
# Sum of numbers using Recursion