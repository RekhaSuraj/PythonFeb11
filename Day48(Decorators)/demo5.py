# with  decorator
# Decorators

'''Decorators are higher order functions because they take in a function and return a
function'''

# A decorator is a function that modifies or enhances the behavior of another function, method, or class without
# modifying its code directly.
#
# Think of it as a wrapper: it takes a function, adds something extra (like logging, timing, authentication checks, etc.),
# and returns a new function with that added behavior.


def outer_fun(name):
    def inner_fun():
        bday = name()
        return bday + ' Wishes on your special day'

    return inner_fun

@outer_fun
def wishes():
    return 'Vittal'

print(wishes())
# Vittal Wishes on your special day

# is same as this:
# ob1 = outer_fun(wishes)
# print(ob1())

#  How It Works:
# outer_fun() is a decorator function. It takes a function Name (in this case, wishes) as input.
#
# Inside outer_fun, it defines inner_fun, which calls the original function (name()), and appends a birthday message to its return value.
#
# The @outer_fun syntax is a decorator shortcut for:
# wishes = outer_fun(wishes)
