set1 = {'hi','hello','Vittal','Aparna',10,20}
print(type(set1))
# <class 'set'>

# copy() - Returns a shallow copy of the set
set2 = set1.copy()
print(set2)
# {'hi', 20, 10, 'Aparna', 'Vittal', 'hello'}

# Return the union of sets as a new set.
# (i. e. all elements that are in either set.)
set3 = {10,'hi',22,44,'welcome'}
set4 = set2.union(set3)
print('set2:',set2)
print('set3:',set3)
print('set4:',set4)

# Return the intersection of two sets as a new set.
# (i. e. all elements that are in both sets.)
set5 = {11,22,44,55,77}
set6 = {44,77,'python','dev'}
set7 = set5.intersection(set6)
print(set7)
# {44, 77}



