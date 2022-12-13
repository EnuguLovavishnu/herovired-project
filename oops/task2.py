# Fetch name,age and salary and display it in the screen.

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def getDetails(self):
        print(f"Hi My Name is{self.name},I recevied {self.marks} marks.")

    def getDetails1(self):
        print(f"Hi My Name is {self.name},I received {self.marks} marks")


stud1=student("srisri",90)
stud2=student("gowrishankar",99)
#method calling
stud1.getDetails()
stud2.getDetails1()
