class Method_Overriding:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    # inbuilt __str__ method is overridden(str, print(), f')
    def __str__(self):
        return f'{self.a},{self.b}'

    # inbuilt __add__ method is overridden(+)
    def __add__(self, other):
        return f'{self.a+other.a},{self.b+other.b}'


obj1 = Method_Overriding(5,7)
print(obj1)


obj2 = Method_Overriding(3,6)
print(obj2)

print(obj1 + obj2)
# 8,13

# This tells Python how to behave when you write obj1 + obj2.
# Instead of the default behavior (which would raise an error), it adds the a and b values from both objects and returns a formatted string.

# Calls __add__:
# self.a = 5, self.b = 7
# other.a = 3, other.b = 6
# Result: 5+3 = 8, 7+6 = 13
# Returns: '8,13'

