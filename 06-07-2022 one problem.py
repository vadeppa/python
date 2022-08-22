'''
Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes.
Print all the attributes of student1, student2 instances with their values in the given format.

Input values of the instances:
student_1:
student_id = "V12"
student_name = "Ernesto Mendez"
student_2:
student_id = "V12"
marks_language = 85
marks_science = 93
marks_math = 95

Expected Output:

student_id -> V12
student_name -> Ernesto Mendez

student_id -> V12
marks_language -> 85
marks_science -> 93
marks_math -> 95
'''
class Student:
    def __init__(self,student_id,student_name,marks_language,marks_science,marks_math):
        self.student_id=student_id
        self.student_name=student_name
        self.marks_language=marks_language
        self.marks_science=marks_science
        self.marks_math=marks_math
    def student1(self):
        print("the student id is :",self.student_id)
        print("the student name is:",self.student_name)
    def student2(self):
        print("the student id is:",self.student_id)
        print("the marks language is;",self.marks_language)
        print("the marks_science is :",self.marks_science)
        print("the marks_math is :",self.marks_math)
obj=Student(22070,'vadeppa',92,82,98)
print("student1 output is\n")
obj.student1()
print("\n")
print("student2 output is\n")
obj.student2()



        
        
        
