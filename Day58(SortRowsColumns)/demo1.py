# DataFrame.select_dtypes

# DataFrame.select_dtypes() is a pandas method used to select columns in a DataFrame based on their data
# syntax:DataFrame.select_dtypes(include=None, exclude=None)
# Parameters:
# include: data types to include (e.g., 'number', 'float', 'int', 'object', 'bool', 'datetime', etc.)
#
# exclude: data types to exclude

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'A':[1,2,3], #int
        'B':[2,4.5,8.9], #Float
        'C':['x','y','z'], #object(string)
        'D':[True,False,True] #Bool
    }
)

print(df)
#    A    B  C      D
# 0  1  2.0  x   True
# 1  2  4.5  y  False
# 2  3  8.9  z   True

# Print only int
print(df.select_dtypes(include=int))
#    A
# 0  1
# 1  2
# 2  3

print(df.select_dtypes(include=float))
#      B
# 0  2.0
# 1  4.5
# 2  8.9

print(df.select_dtypes(include=[object,bool]))

#    C      D
# 0  x   True
# 1  y  False
# 2  z   True

print()
# Exclude - number (int and float)
print(df.select_dtypes(exclude='number'))
#    C      D
# 0  x   True
# 1  y  False
# 2  z   True

#    C      D
# 0  x   True
# 1  y  False
# 2  z   True