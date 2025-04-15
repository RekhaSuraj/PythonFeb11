dict1 = {'dose':'set','idly':'rava','tea':'masala','coffee':'black'}

# copy() - a shallow copy of dictionary and returns a new dictionary
dict2 = dict1.copy()
print(dict2)
# {'dose': 'set', 'idly': 'rava', 'tea': 'masala', 'coffee': 'black'}

# dict2.clear()
dict3 = {1:'GRK',2:'Office'}

# dict2.update({1:'GRK',2:'Office'})
dict2.update(dict3)
print(dict2)
# {'dose': 'set', 'idly': 'rava', 'tea': 'masala', 'coffee': 'black', 1: 'GRK', 2: 'Office'}




