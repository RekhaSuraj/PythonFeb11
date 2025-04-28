# Accessing public method in child class
class Student:

    # instance method - public
    def display_documents(self):
        print('Display original marks card')


class New_student(Student):

    def check_documents(self):
        print('check documents')
        super().display_documents()


ob1 = New_student()
ob1.check_documents()

# check documents
# Display original marks card