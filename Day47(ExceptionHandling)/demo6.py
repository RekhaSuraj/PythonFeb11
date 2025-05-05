# If an exception occurs at any stt and if its not handled, it will go back to the caller - Exception Propogation
import traceback

def f1():
    print('start f1')
    print(10/0)
    print('End f1')


def f2():
    print('start f2')
    f1()
    print('End f2')


def f3():
    print('start f3')
    f2()
    print('End f3')


f3()


# Traceback (most recent call last):
#   File "F:\Rekha\GRKTrainings\PythonFeb11\Day47(ExceptionHandling)\demo6.py", line 19, in <module>
#     f3()
#   File "F:\Rekha\GRKTrainings\PythonFeb11\Day47(ExceptionHandling)\demo6.py", line 15, in f3
#     f2()
#   File "F:\Rekha\GRKTrainings\PythonFeb11\Day47(ExceptionHandling)\demo6.py", line 9, in f2
#     f1()
#   File "F:\Rekha\GRKTrainings\PythonFeb11\Day47(ExceptionHandling)\demo6.py", line 3, in f1
#     print(10/0)
#           ~~^~
# ZeroDivisionError: division by zero
# start f3
# start f2
# start f1
#
# Process finished with exit code 1
