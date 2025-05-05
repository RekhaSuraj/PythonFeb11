#user defined exception:how to create our own exception ?
class MyException(Exception):
    def __init__(self):
        self.message='This is My Exception,number is ZERO'
        super().__init__(self.message)


def f1(n):
    if n==0:
       raise MyException() # generating the exception, use raise keyword

    else:
        print(n)


try:
    n=int(input('please enter a number'))
    f1(n)
except MyException as e:
    print(e)
    print('Sorry')


# please enter a number0
# This is My Exception,number is ZERO
# Sorry

# please enter a number9
# 9