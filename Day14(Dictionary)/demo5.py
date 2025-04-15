dict1 = {'emp':'Vittal','salary':50000,'company':'TSScorp'}

# Fetch a value by giving key
print(dict1['emp'])
# Vittal

# Return the value for key if key is in the dictionary, else default.
# syntax : dict.get(key)
print(dict1.get('emp'))
# Vittal

print(dict1.get('company'))
# TSScorp

# Change/update the value of a key
dict1['emp'] = 'Vittal1'
print(dict1)
# {'emp': 'Vittal1', 'salary': 50000, 'company': 'TSScorp'}

dict1['salary'] = 100000
print(dict1)
# {'emp': 'Vittal1', 'salary': 100000, 'company': 'TSScorp'}