class Person(object):

    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(Person):

    def isEmployee(self):
        return True

Emp=Person("Lova")
print(Emp.getName(),Emp.isEmployee())

Emp1=Employee("Vishnu")
print(Emp1.getName(),Emp1.isEmployee())