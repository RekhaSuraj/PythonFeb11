# Python list and Numpy arrays
# 1.Similarities
# 2.Difference
# 3. Advantages of array

# 1.Similarities :
# a). Both can be used to store data
# b). Order will be preserved in both type.(we can access elements using index)
# c). Slicing is also applicable for both
# d). Both are mutable, once we create list or array.

# 2.Difference
# a1). List is In-built data type but numpy array is not in-built, we have to install
# a2). We can create number of dimensions in numpy array, it is not possible to make Ndimension in list
# a3). List can hold heterogenous (Multiple data types)
#        but Array can hold only homogenous element
# a4). On arrays we can perform vector operations like 1-D, 2-D, 3-D
# (but we cannot perform vector operations on list).

# 3 . Advantage of Array
# a5). Array consuming less memory
# a6). Array super fast when compared with list.
# a7). Numpy array are more convenient to use while performing mathematical operations


# Creating One-Dimensional Array by using UserInput:
import numpy as np
# What is ndarray ?
# In numpy, we can hold data by using array Data structure.
# The array which are created by using numpy are called ndarray
# ndarray --> N-Dimensional Array or NUmpy array
# This ndarray mostly used in DataScience libraries like pandas, scipy etc

array_list = int(input('Enter the size'))
a1 = np.ndarray(shape=[array_list],dtype=int)
for i in range(array_list):
    a1[i] = int(input('Enter element:'))

print('Array elements:',a1)

# Enter the size6
# Enter element:1
# Enter element:2
# Enter element:3
# Enter element:4
# Enter element:5
# Enter element:6

# Array elements: [1 2 3 4 5 6]
print(a1.shape)
print(a1.ndim)
print(a1.size)
# (6,)
# 1
# 6