# QUESTION 6

def student_data(student_id,**kwargs):
    print("Student ID :", student_id)
    if 'student_name' in kwargs:
        print("Student name : ",kwargs['student_name'])
    if 'student_class' in kwargs:
        print("Student class : ",kwargs['student_class'])

student_data(student_id= '21107079',student_name = 'Hemang Bansal')
print()
student_data(student_id= '21107079',student_class = 'Mechanical')
print()
student_data(student_id= '21107079',student_name = 'Hemang Bansal',student_class = 'Mechanical')
