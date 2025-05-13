import numpy as np
import datetime

a1 = np.array([1,2,3,4,5])
a2 = np.array([5,6,7,8,9])


def prod_operation(a,b):
    result = 0
    for v1,v2 in zip(a,b):
        result = result + v1* v2

    return result


start = datetime.datetime.now()
for i in range(10000):
    prod_operation(a1,a2)
end = datetime.datetime.now()
print('Time taken - Normal python:',end-start)

start1 = datetime.datetime.now()
for i in range(10000):
    np.dot(a1,a2)
end1 = datetime.datetime.now()
print('Time taken - dot function:',end1-start1)

# Numpy array dot function is faster now.
# Time taken - Normal python: 0:00:00.044004
# Time taken - dot function: 0:00:00.011719