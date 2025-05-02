import os

print(os.getcwd())
# F:\Rekha\GRKTrainings\PythonFeb11\Day45(OSModule)

# To create a new directory

# os.chdir("F:\\Rekha\\GRKTrainings\\Demo\\All Notes")
# print(os.getcwd())
# os.mkdir() - Create a directory
# Following method can also be done or we can chdir and then just give folder name
# os.mkdir("F:\\Rekha\\GRKTrainings\\Demo\\All Notes\\os-module")
# os.mkdir("os1-module")
# FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'os1-module'

# remove or delete a directory
os.rmdir("F:\\Rekha\\GRKTrainings\\Demo\\All Notes\\os-module")

print(os.listdir())
# ['demo1.py', 'demo2.py']
