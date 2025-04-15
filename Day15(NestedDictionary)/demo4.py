# create a dictionary using 2 lists
names = ['Vittal','Aparna','Raju','John']
age = [20,21,22,23]

# {'Vittal':20,'Aparna':21,'Raju':22,'John':23}
# zip()
# print(help(zip))
v1 = dict(zip(names,age))
# v1 = tuple(zip(names,age))
print(v1)

# {'Vittal': 20, 'Aparna': 21, 'Raju': 22, 'John': 23}



