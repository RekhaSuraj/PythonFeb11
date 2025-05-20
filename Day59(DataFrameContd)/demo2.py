# Rename columns in csv file
import pandas as pd

df1 = pd.read_csv('emp.csv')

cols = df1.columns
print(cols)
# Index(['EmpId', 'EmpName', 'EmpLoc', 'EmpSal'], dtype='object')

# List of columns
print(df1.columns.values)
# ['EmpId' 'EmpName' 'EmpLoc' 'EmpSal']
print(df1)
print()
# Rename EmpLoc to EmpLocation
print(df1.rename(columns={'EmpLoc':'EmpLocation'}))
# EmpLoc renamed to EmpLocation

#    EmpId  EmpName EmpLocation  EmpSal
# 0      1   Aparna         BLR   50000
# 1      2   Vittal         BTM   60000
# 2      3     Rama          AP   70000
# 3      4  Krishna         IND   80000
# 4      5   Seetha          UK   90000

print()
# EmpLoc is unchanged in my original dataframe
print(df1)

print()
# If we want to rename the original df, give inplace = True
df1.rename(columns={'EmpLoc':'EmpLocation'},inplace=True)
print(df1)

#    EmpId  EmpName EmpLocation  EmpSal
# 0      1   Aparna         BLR   50000
# 1      2   Vittal         BTM   60000
# 2      3     Rama          AP   70000
# 3      4  Krishna         IND   80000
# 4      5   Seetha          UK   90000