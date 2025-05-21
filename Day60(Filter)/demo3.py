import pandas as pd

df = pd.read_csv('Emp.csv')
# duplicated()
# The DataFrame.duplicated() method in pandas is used to identify duplicate rows in a DataFrame.
# Parameters:
# subset (optional): Column label(s) to consider for identifying duplicates. Default is None, meaning all columns are used.
# keep (optional):
# 'first' (default): Mark duplicates except the first occurrence as True.
# 'last': Mark duplicates except the last occurrence as True.
# False: Mark all duplicates as True.
# A Boolean Series where True indicates a duplicate row.

print(df)
print()
print(df.duplicated(subset=['Esalary']))

# .loc
# The .loc[] accessor in Pandas is used to access or modify data in a DataFrame by
# label-based indexing — that is, by row labels and column names.
# It is used to access a group of rows and columns by labels or a boolean array.

print()
# print(df.loc[2])

# Emp_id                  13
# Ename        pramood kumar
# Eage                    27
# Esalary              50000
# Elocation           mumbai
# Name: 2, dtype: object

# Fetch 3rd and 5th rows - 2d
# print(df.loc[[3,5]])
#    Emp_id          Ename  Eage  Esalary Elocation
# 3      14         vishal    23    20000     delhi
# 5      16  Hareesh kumar    23    45000      Agra

print()
print(df.loc[1:3,['Ename','Esalary']])

#            Ename  Esalary
# 1   madhavan DOn    40000
# 2  pramood kumar    50000
# 3         vishal    20000

# update values using loc
# Update Elocation of Empid 17 to bangalore
# syntax : df.loc[row_condition, 'column_name'] = new_value

df.loc[df['Emp_id']==17, 'Elocation'] = 'bangalore'
print(df)
#    Emp_id          Ename  Eage  Esalary  Elocation
# 0      11     Ravi kumar    21    34000    chennai
# 1      12   madhavan DOn    23    40000       pune
# 2      13  pramood kumar    27    50000     mumbai
# 3      14         vishal    23    20000      delhi
# 4      15       sireesha    22    30000     kerala
# 5      16  Hareesh kumar    23    45000       Agra
# 6      17          Darla    22    50000  bangalore
# 7      18         Dinesh    23    30000     kerala
# 8      19       santhosh    22    25000   banglore
# 9      20        micheal    25    34000  hyderabad


# update age of EmpId 12
print()
df.loc[df['Emp_id'] == 12, 'Eage'] = 25
print(df)



