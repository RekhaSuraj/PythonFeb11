d1 = {'student_name1':'Vittal','student_name2':'Aparna','student_name3':'Rama','student_name4':'Seetha'}

# updating the key to a new value
d1['stu_name'] = d1.pop('student_name3')
print(d1)

# {'student_name1': 'Vittal', 'student_name2': 'Aparna', 'student_name4': 'Seetha', 'stu_name': 'Rama'}


