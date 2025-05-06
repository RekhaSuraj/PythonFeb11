# 2). Passing Function as an Argument in Python

def square_num():
    return 5**2


def cube_num():
    return 6**3

# Passing function as an argument. Here num is nothing but function object(square_num or cube_num)
def check(num):
    print(num()) #square_num()

check(square_num)
check(cube_num)