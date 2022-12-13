class Employee:
    def __init__(self):
        print("employee creator")
      

    def __del__(self):
        print('Destructor called employee deleted')

emp = Employee()
del emp
# emp = Employee()
