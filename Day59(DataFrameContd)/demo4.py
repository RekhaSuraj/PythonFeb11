# Remove or drop a column or row

import pandas as pd
d1 = pd.read_csv('emp.csv')
print(d1.columns)
print(d1)
print()
print(d1.drop('EmpLoc',axis=1))

#    EmpId  EmpName  EmpSal
# 0      1   Aparna   50000
# 1      2   Vittal   60000
# 2      3     Rama   70000
# 3      4  Krishna   80000
# 4      5   Seetha   90000

print()
# remove a row - 3rd index is dropped
print(d1.drop(3,axis=0))

#    EmpId EmpName EmpLoc  EmpSal
# 0      1  Aparna    BLR   50000
# 1      2  Vittal    BTM   60000
# 2      3    Rama     AP   70000
# 4      5  Seetha     UK   90000

print(d1)
# original df still has index 3 record
#    EmpId  EmpName EmpLoc  EmpSal
# 0      1   Aparna    BLR   50000
# 1      2   Vittal    BTM   60000
# 2      3     Rama     AP   70000
# 3      4  Krishna    IND   80000
# 4      5   Seetha     UK   90000

print()
# updates the changes permanently inplace=True
d1.drop(3,axis=0,inplace=True)
print(d1)

#    EmpId EmpName EmpLoc  EmpSal
# 0      1  Aparna    BLR   50000
# 1      2  Vittal    BTM   60000
# 2      3    Rama     AP   70000
# 4      5  Seetha     UK   90000