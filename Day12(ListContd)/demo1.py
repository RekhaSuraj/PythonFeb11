# List sort (Ordering)
# sort() - sorts the original list in ascending order by default

list1 = [40,10,20,51,32,12,10]
list1.sort()
print(list1)
# [10, 10, 12, 20, 32, 40, 51]

list1.sort(reverse=True)
print(list1)
# [51, 40, 32, 20, 12, 10, 10]

# sorted() - Return a new list containing all items from the iterable in ascending order

list2 = [90,30,10,2,5,1,17]
print(sorted(list2))
# [1, 2, 5, 10, 17, 30, 90]

list3 = sorted(list2)
print('list3',list3)
# list3

print('list2',list2)
# list2 [90, 30, 10, 2, 5, 1, 17]

# Key Differences:
# Feature	                    sort()	            sorted()
#
# Modifies original list?	    ✅ Yes	            ❌ No
# Returns new list?	            ❌ No	            ✅ Yes
# Works with lists only?	    ✅ Yes	            ❌ No (works with any iterable)
# Memory efficient?	            ✅ Yes	            ❌ No (creates new object)