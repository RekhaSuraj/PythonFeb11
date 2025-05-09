import array
import sys

l1 = [1,2,3,4,5]

a1 = array.array('i',[1,2,3,4,5])

print('Memory size:List',sys.getsizeof(l1))
print('Memory size:array',sys.getsizeof(a1))

# Array takes less memory size than list
# Memory size:List 104
# Memory size:array 100

# signed integer 'b'
a2 = array.array('b',[])
a3 = array.array('b',[1])
a4 = array.array('b',[1,2])

print('Empty array memory size:',sys.getsizeof(a2))
print('1 byte array memory size:',sys.getsizeof(a3))
print('2 byte array memory size:',sys.getsizeof(a4))

# Empty array memory size: 80
# 1 byte array memory size: 81
# 2 byte array memory size: 82

a2.append(4)
print(a2)
# array('b', [4])

a4.pop(1)
print(a4)
# array('b', [1])

a5 = array.array('b',[1,2,-3])
print(a5)
# array('b', [1, 2, -3])