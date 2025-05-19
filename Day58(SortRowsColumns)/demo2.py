import numpy as np
import pandas as pd

# Sort rows and columns
# Sort rows

d1 = pd.DataFrame(
    {
        'A':[10,11,12,np.nan,13,14],
        'B':[20,21,np.nan,23,24,25],
        'C':[30,31,32,33,34,np.nan]
    }
)

print(d1)
print()
# sort rows based on index
# axis=0 , means row sorting
# print(d1.sort_index(axis=0,ascending=False))

#       A     B     C
# 5  14.0  25.0   NaN
# 4  13.0  24.0  34.0
# 3   NaN  23.0  33.0
# 2  12.0   NaN  32.0
# 1  11.0  21.0  31.0
# 0  10.0  20.0  30.0

print()
# sort rows by values
print(d1.sort_values(by='A',axis=0,ascending=False))
# also
# Below gives the same result
# print(d1.sort_values('A',axis=0,ascending=False))
#       A     B     C
# 5  14.0  25.0   NaN
# 4  13.0  24.0  34.0
# 2  12.0   NaN  32.0
# 1  11.0  21.0  31.0
# 0  10.0  20.0  30.0
# 3   NaN  23.0  33.0



