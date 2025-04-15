dict1 = {'Mangoes':10,'Oranges':6,'Apples':4,'Grapes':15}

for k in dict1:
    print(k)

# Mangoes
# Oranges
# Apples
# Grapes

# items() - a set-like object providing a view on D's items
for v in dict1.items():
    print(v)

# ('Mangoes', 10)
# ('Oranges', 6)
# ('Apples', 4)
# ('Grapes', 15)


for k,v in dict1.items():
    print(k,v)

# Mangoes 10
# Oranges 6
# Apples 4
# Grapes 15

for k in dict1:
    print(dict1[k])
#
# 10
# 6
# 4
# 15

# Doubling the dictionary values
for k in dict1:
    dict1[k] = dict1[k] * 2

print(dict1)
# {'Mangoes': 20, 'Oranges': 12, 'Apples': 8, 'Grapes': 30}


