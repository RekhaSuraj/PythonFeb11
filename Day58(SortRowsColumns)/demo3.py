import pandas as pd
import numpy as np

# Sort Columns - axis = 1
d1 = pd.DataFrame(
    {
        'A':[10,11,12,np.nan,13,14],
        'B':[20,21,np.nan,23,24,25],
        'C':[30,3,32,33,34,np.nan]
    }
)

print(d1)
#       A     B     C
# 0  10.0  20.0  30.0
# 1  11.0  21.0  31.0
# 2  12.0   NaN  32.0
# 3   NaN  23.0  33.0
# 4  13.0  24.0  34.0
# 5  14.0  25.0   NaN

# print(d1.sort_index(axis=1,ascending=False))

#       C     B     A
# 0  30.0  20.0  10.0
# 1  31.0  21.0  11.0
# 2  32.0   NaN  12.0
# 3  33.0  23.0   NaN
# 4  34.0  24.0  13.0
# 5   NaN  25.0  14.0

print()
# Sort values
# print(d1.sort_values(by=1,ascending=False,axis=1))
# Row 1 values
# B - 21.0
# A - 11.0
# C - 3.0

#       B     A     C
# 0  20.0  10.0  30.0
# 1  21.0  11.0   3.0
# 2   NaN  12.0  32.0
# 3  23.0   NaN  33.0
# 4  24.0  13.0  34.0
# 5  25.0  14.0   NaN

print()
print(d1.sort_values(by=5,axis=1,ascending=False))
# Row 5 values
# B - 25.0
# A - 14.0
# C - Nan

#       B     A     C
# 0  20.0  10.0  30.0
# 1  21.0  11.0   3.0
# 2   NaN  12.0  32.0
# 3  23.0   NaN  33.0
# 4  24.0  13.0  34.0
# 5  25.0  14.0   NaN