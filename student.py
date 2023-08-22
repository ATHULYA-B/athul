class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
        
    def display(self):
        print("name",self.name)
        print("rollno",self.rollno)
        print("age",self.age)
        print("mark",self.mark)
    def setage(self,age):
        self.age=age
    def setmark(self,mark):
        self.mark=mark
name=(input("enter the name of the student"))
rollno=int(input("enter the rollno of the student"))
student1=Student(name,rollno)

age=int(input("enter the age of the student"))
marks=float(input("enter student marks"))
student1.setage(age)
student1.setmark(marks)
student1.display()