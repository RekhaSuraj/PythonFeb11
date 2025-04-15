# update - Update a set with the union of itself and others. Concatenates 2 sets
set1 = {10,203,30,40,50}
set1.update({60,70})

print(set1)
# {50, 70, 40, 10, 203, 60, 30}

set2 = {99,100}
set1.update(set2)
print(set1)
# {99, 100, 70, 40, 10, 203, 50, 60, 30}

# set1.difference()
# set1.remove()
# set1.clear()



