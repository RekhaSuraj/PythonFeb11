# convert to upper - without decorator

def upper_fun(definition):
    def inner_fun():
        v1 = definition()
        return v1.upper()

    return inner_fun


def definition():
    return 'Python is a high level programming language'

ob1 = upper_fun(definition)
print(ob1())

# PYTHON IS A HIGH LEVEL PROGRAMMING LANGUAGE