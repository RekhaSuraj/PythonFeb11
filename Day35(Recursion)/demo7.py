class Car:
    car_Name = 'Toyota'
    car_Color = 'Black'
    car_Price = 2000000
    car_Type = "Petrol"

car_obj = Car()
print(car_obj.car_Name)
print(car_obj.car_Color)
print(car_obj.car_Price)
print(car_obj.car_Type)

print()

# Update the values
car_obj.car_Type = 'Diesel'
car_obj.car_Color = "White"

# Print
print(car_obj.car_Name)
print(car_obj.car_Color)
print(car_obj.car_Price)
print(car_obj.car_Type)

# lambda if condition
list1 = [2,3,1,4,6,8,7]
print((lambda a:'even number' if a%2==0 else 'odd number')(6))

# using filter
def even_num(n):
    if n%2 == 0:
        return n

print(list(filter(even_num,list1)))

# using lambda
print(tuple(filter(lambda a:a%2 == 0,list1)))

# start with A
list2 = ['Ajay','Amar','Joy','Tim','Aarush']
def start_A(c):
    if c[0].lower()=='a':
        return c[0]

print(list(filter(start_A,list2)))

# using lambda
print(tuple(filter(lambda x:x if x[0].lower()=='a' else "",list2)))

# print in a range using lambda
print(list(filter(lambda a:a%2!=0,range(10))))

# square these numbers
print(list(map(lambda x:x**2,list(filter(lambda a:a%2!=0,range(10))))))

# max of these numbers
print(max(list(map(lambda x:x**2,list(filter(lambda a:a%2!=0,range(10)))))))

# sum of these numbers
print(sum(list(map(lambda x:x**2,list(filter(lambda a:a%2!=0,range(10)))))))






