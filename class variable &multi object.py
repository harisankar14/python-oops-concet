''' fields belongs to class
and fields have two things 1) instance variable   2)class variable

1)instance variable- the variable belongs to instance/object
2)class variable-the variable belongs to the class '''

class student:
    clg="vitam"  #class variable (this value is same for all the objects i.e. created)
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print("student name:",self.name)
        print("student rollnoo:",self.rollno)
        print("student college:",self.clg)

student1=student("hari",12)
student2=student("manoj",35)
student3=student("Anil",27)

student1.display()
student2.display()
student3.display()
