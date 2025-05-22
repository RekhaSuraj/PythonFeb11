import pandas as pd

df = pd.read_csv('Emp.csv')
print(df)
print()
# print(df.duplicated(subset='Esalary'))
# print(df.loc[df.duplicated(subset='Esalary')])

#    Emp_id    Ename  Eage  Esalary  Elocation
# 6      17    Darla    22    50000     ladakh
# 7      18   Dinesh    23    30000     kerala
# 9      20  micheal    25    34000  hyderabad

# keep="first" is default- Mark duplicates except the first occurrence as True.

# print(df.duplicated(subset='Esalary',keep="last"))
print()
# 'last': Mark duplicates except the last occurrence as True.
print(df.loc[df.duplicated(subset='Esalary',keep="first")])

# age
# print(df.duplicated(subset='Eage',keep="last"))
print()
# print(df.loc[df.duplicated(subset='Eage',keep="first")])