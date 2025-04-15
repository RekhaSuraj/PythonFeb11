# count the number of alphabets in a string
str1 = 'Hello Worlde'
str2 = str1.replace(" ","")
print(str2)

res_dict = {}
for s in str2:
    if s in res_dict:
        res_dict[s] = res_dict[s] + 1
    else:
        res_dict[s] = 1

print(res_dict)
# {'H': 1, 'e': 2, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1}

# displaying only duplicates from the above dictonary
dup_dict = {}
for v in res_dict:
    if res_dict[v] > 1:
        dup_dict[v] = res_dict[v]

print('Duplicates dict:',dup_dict)
# Duplicates dict: {'e': 2, 'l': 3, 'o': 2}






