
# Decorators is a higher-order functions that function operates another function
# either as a argument and function object.

# Without decoarator
def fun1(name):
    def inner_fun():
        bday = name() #wishes()
        return bday + ' I wish you on your special day'

    return inner_fun


def wishes():
    return 'Aparna'

ob1 = fun1(wishes)
print(ob1())

# Aparna I wish you on your special day
