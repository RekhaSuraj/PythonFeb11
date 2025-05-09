import array
import sys

# 'u' unicode character - 2
a1 = array.array('u',['a','b','c'])
print(a1)
# array('u', 'abc')
print(sys.getsizeof(a1))
# 86
a1.pop(0)
print(a1)
# array('u', 'bc')

# d - 8
a2 = array.array('d',[1,2,3,4,5])
print('Memory size:',sys.getsizeof(a2))
# Memory size: 120

print(a2[3])
# 4.0

# to find the length
print(len(a2))
# 5


# | Feature             | Signed Integer             | Unsigned Integer                    |
# | ------------------- | -------------------------- | ----------------------------------- |
# | Supports negatives  | ✅ Yes                      | ❌ No                                |
# | Value range (8-bit) | -128 to +127               | 0 to 255                            |
# | Storage size        | Same (e.g., 1 byte)        | Same                                |
# | Use cases           | Temperatures, gains/losses | Memory addresses, sizes, RGB values |
#
# Think of an 8-bit unsigned int like a ruler with 256 units (0 to 255), and a signed int like a ruler centered at 0,
# ranging from -128 to 127.
#



