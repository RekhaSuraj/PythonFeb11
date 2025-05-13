import numpy as np
import array
import datetime

a1 = array.array('i',[1,2,3,4,5])
a2 = array.array('i',[5,6,7,8,9])

def prod_operation(a,b):
    result = 0
    for v1,v2 in zip(a,b):
        result = result + v1* v2

    return result


start = datetime.datetime.now()
for i in range(10000):
    prod_operation(a1,a2)
end = datetime.datetime.now()
print('time taken normal array:',end-start)
# 115

start1 = datetime.datetime.now()
for i in range(10000):
    np.dot(a1,a2)
end1 = datetime.datetime.now()
print('time taken dot product:',end1-start1)
# 115

# Normal array time taken is lesser than Numpy dot() - dot() product is taking time to convert
# normal array to Numpy array
# time taken normal array: 0:00:00.010617
# time taken dot product: 0:00:00.024817

