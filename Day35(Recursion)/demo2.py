# Program to add numbers

def print_num(num): # function definition
    if num <= 0: # Exit case(base case)
        print('End')
    else:
        print(num)
        num = num - 1
        print_num(num) # Recursive case

print_num(5)

# 5
# 4
# 3
# 2
# 1
# End

