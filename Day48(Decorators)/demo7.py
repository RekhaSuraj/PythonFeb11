# with decorator

def upper_fun(definition):
    def inner_fun():
        v1 = definition()
        return v1.upper()

    return inner_fun

@upper_fun
def definition():
    return 'Python is a high level programming language'

print(definition())

# PYTHON IS A HIGH LEVEL PROGRAMMING LANGUAGE