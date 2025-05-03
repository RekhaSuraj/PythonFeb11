import datetime
# create a file with current date and time as its name

dt = datetime.datetime.now()
print(dt)
file_name = dt.strftime('%Y-%m-%d_%H-%M-%S.txt')
print(file_name)

with open(file_name,'w') as file:
    file.write(f'Hello- This file is Created on {dt.strftime('%Y-%m-%d_%H-%M-%S')}')


# Hello- This file is Created on 2025-05-03_10-46-55