import csv
# CSV - Comma Separated Values

# CSV Files:

# Python CSV
# A CSV (Comma Separated Values) format is one of the most simple and common ways to store tabular data.
# To represent a CSV file, it must be saved with the .csv file extension.


# Working with CSV files in Python
# While we could use the built-in open() function to work with CSV files in Python,
# there is a dedicated csv module that makes working with CSV files much easier.


with open('emp.csv','w',newline='') as file:
    info1 = csv.writer(file)

    info1.writerow(['EmpId','EmpName','EmpLoc','EmpSal'])
    while True:
        emp_Id = int(input('Enter your ID'))
        emp_Name = input('Enter your name')
        emp_Loc = input('Enter your location')
        emp_Sal = int(input('Enter your salary'))

        info1.writerow([emp_Id,emp_Name,emp_Loc,emp_Sal])
        user_input = input('Do you want to insert one more record YES|No?')
        if user_input.lower() == 'no':
            break

