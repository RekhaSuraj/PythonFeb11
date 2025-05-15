import numpy as np
import pandas as pd

# np.nan is a special floating-point value defined in the IEEE 754 standard.
# It is used to mark missing, undefined, or null values.
# It is of type float.

p1 = pd.Series([1,2,3,np.nan,4,np.nan,5])
print(p1)
# 0    1.0
# 1    2.0
# 2    3.0
# 3    NaN
# 4    4.0
# 5    NaN
# 6    5.0
# dtype: float64

print()
p2 = pd.Series([1,2,3,np.nan,4,np.nan,5],name='Numbers')
print(p2)

# 0    1.0
# 1    2.0
# 2    3.0
# 3    NaN
# 4    4.0
# 5    NaN
# 6    5.0
# Name: Numbers, dtype: float64