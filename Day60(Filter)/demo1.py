import pandas as pd

df = pd.read_csv('Emp.csv')
print(df)
print()
# To print only names
# print(df['Ename'])

# Filter based on salary - bool
sal = df['Esalary'] > 30000
# print(sal)

print()
# print(df[sal])

# print directly
print(df[df['Esalary'] > 30000])

#    Emp_id          Ename  Eage  Esalary  Elocation
# 0      11     Ravi kumar    21    34000    chennai
# 1      12   madhavan DOn    23    40000       pune
# 2      13  pramood kumar    27    50000     mumbai
# 5      16  Hareesh kumar    23    45000       Agra
# 6      17          Darla    22    50000     ladakh
# 9      20        micheal    25    34000  hyderabad





