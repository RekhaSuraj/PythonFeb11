# print odd numbers from 1 to 15 using lambda

print(list(filter(lambda x: x%2 != 0, range(1,16))))
# [1, 3, 5, 7, 9, 11, 13, 15]

# Square of odd numbers
print(tuple(map(lambda a:a**2, list(filter(lambda x: x%2 != 0, range(1,16))))))

# max number in the list
print(max(tuple(map(lambda a:a**2, list(filter(lambda x: x%2 != 0, range(1,16)))))))

# sum of all numbers
print(sum(map(lambda a:a**2, list(filter(lambda x:x%2 != 0, range(1,16))))))

