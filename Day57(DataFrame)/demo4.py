import array

import numpy as np
import pandas as pd
# 4. From an array

a1 = array.array('i',[1,2,3,4,5])

# s1 = pd.DataFrame(data=a1)
# print(s1)
# AttributeError: 'array.array' object has no attribute 'dtype'

# We can convert to a list or a numpy array
s2 = pd.DataFrame(data=list(a1))
print(s2)

#    0
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5


print()
s3 = pd.DataFrame(data=np.array(a1))
print(s3)

#    0
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5
