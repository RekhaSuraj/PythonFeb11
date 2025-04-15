# Nested Dictionary - Dictionary inside another dictionary

# sy : {key : {key:value},
#       key: {key : value}
#       }


d1 = {1: {2:'Kar',3:'AP',4:'MP'},
      5: {6:'Delhi',7:'UP'}
      }

print(d1.keys())
# dict_keys([1, 5])

print(d1.values())
# dict_values([{2: 'Kar', 3: 'AP', 4: 'MP'}, {6: 'Delhi', 7: 'UP'}])

print(d1[1].keys())
# dict_keys([2, 3, 4])

print(d1[1].values())
# dict_values(['Kar', 'AP', 'MP'])

print(d1[5].keys())
# dict_keys([6, 7])

print(d1[5].values())
# dict_values(['Delhi', 'UP'])

# print UP
