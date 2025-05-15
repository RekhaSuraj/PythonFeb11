import pandas as pd
# Index : If we don't index labels pandas, Series class will defaultly take indexes  (from 0 to N)
# Custom indexing
print()
p1 = pd.Series([10,20,30,'hello','hi','Welcome'],index=[1,2,3,4,5,6])
print(p1)

# 1         10
# 2         20
# 3         30
# 4      hello
# 5         hi
# 6    Welcome
# dtype: object

print()
p2 = pd.Series(['Vittal','Aparna','Rama','Seetha'],index=['n1','n2','n3','n4'])
print(p2)

# n1    Vittal
# n2    Aparna
# n3      Rama
# n4    Seetha
# dtype: object

