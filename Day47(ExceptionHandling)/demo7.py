import traceback

def f1():
    print('start f1')
    print(10/0)
    print('end f1')

def f2():
    print('start f2')
    f1()
    print('end f2')

def f3():
    print('start f3')
    try:
        f2()
    except:
        print("sorry")
        traceback.print_exc()
    print('end f3')

f3()

# Traceback (most recent call last):
#   File "F:\Rekha\GRKTrainings\PythonFeb11\Day47(ExceptionHandling)\demo7.py", line 17, in f3
#     f2()
#   File "F:\Rekha\GRKTrainings\PythonFeb11\Day47(ExceptionHandling)\demo7.py", line 11, in f2
#     f1()
#   File "F:\Rekha\GRKTrainings\PythonFeb11\Day47(ExceptionHandling)\demo7.py", line 6, in f1
#     print(10/0)
#           ~~^~
# ZeroDivisionError: division by zero
# start f3
# start f2
# start f1
# sorry
# end f3
#
# Process finished with exit code 0