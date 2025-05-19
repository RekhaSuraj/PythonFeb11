# Transpose
import pandas as pd

# Converts rows into columns and columns into rows
# The index becomes the column headers and vice versa

df = pd.DataFrame(
    {
        'A':[20,30,40.5],
        'B':[50,60.5,70],
        'C':[80.5,90,9]
    }

)

print(df)

#       A     B     C
# 0  20.0  50.0  80.5
# 1  30.0  60.5  90.0
# 2  40.5  70.0  9

print()
print(df.T)

dfT = df.T
#       0     1     2
# A  20.0  30.0  40.5
# B  50.0  60.5  70.0
# C  80.5  90.0  90.5
print()
print(dfT.sort_index(axis=0,ascending=False))

#       0     1     2
# C  80.5  90.0  90.5
# B  50.0  60.5  70.0
# A  20.0  30.0  40.5

print()
print(dfT.sort_values(axis=0, by=2,ascending=False))

#       0     1     2
# B  50.0  60.5  70.0
# A  20.0  30.0  40.5
# C  80.5  90.0   9.0


