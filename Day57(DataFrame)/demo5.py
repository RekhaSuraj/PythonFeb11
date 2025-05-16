import pandas as pd

d1 = pd.DataFrame(
    {
        'Names':['Vittal','Aparna','Rama','Seetha','Krishna','GRK','Maniyamma','Sandhya','Uday'],
        'Ages':[20,21,22,23,24,25,26,27,28]
     }
)

print(d1)

#        Names  Ages
# 0     Vittal    20
# 1     Aparna    21
# 2       Rama    22
# 3     Seetha    23
# 4    Krishna    24
# 5        GRK    25
# 6  Maniyamma    26
# 7    Sandhya    27
# 8       Uday    28

# Return the first 5 rows of data
# Dataframe.head() - By default 5 records are displayed
print()
print(d1.head())

#      Names  Ages
# 0   Vittal    20
# 1   Aparna    21
# 2     Rama    22
# 3   Seetha    23
# 4  Krishna    24

print()
print(d1.head(6)) # number of records to be displayed

#      Names  Ages
# 0   Vittal    20
# 1   Aparna    21
# 2     Rama    22
# 3   Seetha    23
# 4  Krishna    24
# 5      GRK    25

# To display last n rows
# Dataframe.tail()
# # This function returns last n rows from the object based on position.
# It is useful for quickly verifying data, for example, after sorting or appending rows.
# By default 5 records are displayed
print()
print(d1.tail())

#        Names  Ages
# 4    Krishna    24
# 5        GRK    25
# 6  Maniyamma    26
# 7    Sandhya    27
# 8       Uday    28

print()
print(d1.tail(2))
#      Names  Ages
# 7  Sandhya    27
# 8     Uday    28

# - ve indexing - For negative values of n, this function returns all rows except the first |n| rows,
# equivalent to df[|n|:].
print()
print(d1.head(-2))

#       Names  Ages
# 0     Vittal    20
# 1     Aparna    21
# 2       Rama    22
# 3     Seetha    23
# 4    Krishna    24
# 5        GRK    25
# 6  Maniyamma    26

print()
print(d1.tail(-2))

#        Names  Ages
# 2       Rama    22
# 3     Seetha    23
# 4    Krishna    24
# 5        GRK    25
# 6  Maniyamma    26
# 7    Sandhya    27
# 8       Uday    28

print()
print(d1.head(-2).tail(-2))

#        Names  Ages
# 2       Rama    22
# 3     Seetha    23
# 4    Krishna    24
# 5        GRK    25
# 6  Maniyamma    26

# slicing
print()
print(d1[0:2])

#     Names  Ages
# 0  Vittal    20
# 1  Aparna    21

print()
print(d1[0:6:2])
#      Names  Ages
# 0   Vittal    20
# 2     Rama    22
# 4  Krishna    24

# Indexing can be customized by giving Dataframe.index = pd.RangeIndex(start,stop,step)
d1.index = pd.RangeIndex(start=10,stop=19)
print(d1)

#         Names  Ages
# 10     Vittal    20
# 11     Aparna    21
# 12       Rama    22
# 13     Seetha    23
# 14    Krishna    24
# 15        GRK    25
# 16  Maniyamma    26
# 17    Sandhya    27
# 18       Uday    28

# Individual columns can be printed
print()
print(d1['Names'])

# 10       Vittal
# 11       Aparna
# 12         Rama
# 13       Seetha
# 14      Krishna
# 15          GRK
# 16    Maniyamma
# 17      Sandhya
# 18         Uday
# Name: Names, dtype: object

print()
print(d1['Ages'])

# 10    20
# 11    21
# 12    22
# 13    23
# 14    24
# 15    25
# 16    26
# 17    27
# 18    28
# Name: Ages, dtype: int64