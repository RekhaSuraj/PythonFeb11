# If we want to rename and override all the column names, then
import pandas as pd

df = pd.read_csv('emp.csv')
print(df)
#    EmpId  EmpName EmpLoc  EmpSal
# 0      1   Aparna    BLR   50000
# 1      2   Vittal    BTM   60000
# 2      3     Rama     AP   70000
# 3      4  Krishna    IND   80000
# 4      5   Seetha     UK   90000

print()
new_cols = ['Emp_ID','Emp_Name','Emp_Location','Emp_Salary']
df.columns = new_cols
print(df)


#    Emp_ID Emp_Name Emp_Location  Emp_Salary
# 0       1   Aparna          BLR       50000
# 1       2   Vittal          BTM       60000
# 2       3     Rama           AP       70000
# 3       4  Krishna          IND       80000
# 4       5   Seetha           UK       90000

print()
# While reading a csv file itself, we can rename columns
new_cols = ['Emp_ID','Emp_Name','Emp_Location','Emp_Salary']
df2 = pd.read_csv('emp.csv',names=new_cols)
print(df2)

#   Emp_ID Emp_Name Emp_Location Emp_Salary
# 0  EmpId  EmpName       EmpLoc     EmpSal
# 1      1   Aparna          BLR      50000
# 2      2   Vittal          BTM      60000
# 3      3     Rama           AP      70000
# 4      4  Krishna          IND      80000
# 5      5   Seetha           UK      90000