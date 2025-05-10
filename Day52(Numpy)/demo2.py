import array
import numpy as np

# array
a1 = array.array('i',[1,2,3,4,5])
print(type(a1))
# <class 'array.array'>

# list
l1 = [1,2,3,4,5]
print(type(l1))
# <class 'list'>

a2 = array.array('i',l1)
print(type(a2))
# <class 'array.array'>

# numpy array
# syntax: modulename.function()
n1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(type(n1))
# <class 'numpy.ndarray'>

# print(help(np.array))
# array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,
#       like=None)

# Properties of Numpy
print('Size:',n1.size)
print('NDim:',n1.ndim)
print('Datatype:',n1.dtype)
print('Shape:',n1.shape)
print('ItemSize:',n1.itemsize)

# Size: 10
# NDim: 1
# Datatype: int64
# Shape: (10,)
# ItemSize: 8

