# Create a class - Employee for two employees with some objects. 

# this is creating a class
class Employee:
    # This is  class attribute
    company="Aditya college" 

    def __init__(self,name,age,salary):#default constructor
        #name,age,salary are attributes
        self.name=name
        self.age=age
        self.salary=salary

#creating objects
emp1=Employee("Lovavishnu",22,40000)
emp2=Employee("naveen",22,50000)

print(f"{emp1.name} and {emp2.name} works in {emp1.__class__.company}")# formated string
print(f"{emp1.name}'s age is {emp1.age} and salary is{emp1.salary}")
print(f"{emp2.name}'s age is {emp2.age} and salary is{emp2.salary}")

# Fetch name,age and salary and display it in the screen.







