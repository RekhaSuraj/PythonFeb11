# Pandas

# pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
# built on top of the Python programming language.

import pandas as pd
# TO check version in your Environment
print('Current Version :', pd.__version__)
# Current Version : 2.2.3

# Basic data structures in pandas
# Pandas provides two types of classes for handling data:
#
# Series: a one-dimensional labeled array holding data of any type
# such as integers, strings, Python objects etc.
#
# DataFrame: a two-dimensional data structure that holds data like a two-dimension array or a table with
# rows and columns.

l1 = [1,2,3,4,5]
p1 = pd.Series(data=l1,dtype='int64')
print(type(p1))
# <class 'pandas.core.series.Series'>
print(p1)

# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64