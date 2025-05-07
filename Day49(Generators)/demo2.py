# Generator:

# What is Generator ?

# A generator is a special type of function that yields values one at a time using the yield keyword instead of
# returning all of them at once with return.
# Generators are:
# Memory efficient (do not store all values in memory)
# Lazy (generate values only when requested)
# Iterators (can be used in a for loop or with next())

# syn:
# def Generate():
    # yield value.....1

def fun():
    return 'hello world'


print(type(fun))
# <class 'function'>

# Explanation:
# gen_fun() is a generator function.
# When you call gen_fun(), it doesn't execute the function immediately. Instead, it returns a generator object, stored in ob1.
# You can retrieve the values using:
# The next() function
# A for loop


def gen_fun():
    yield 10
    yield 20
    yield 30

print(type(gen_fun()))
# <class 'generator'>
ob1 = gen_fun()
print(ob1)
# <generator object gen_fun at 0x000001594B194B40>
print(type(ob1))
# <class 'generator'>
# print(ob1())
# TypeError: 'generator' object is not callable

# So to fetch values, we can use next(ob1)
print(next(ob1))
# 10

print(next(ob1))
# 20

print(next(ob1))
# 30

# If we try to access next after all elements, we get the below error
# print(next(ob1))
# StopIteration

