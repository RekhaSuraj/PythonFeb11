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
