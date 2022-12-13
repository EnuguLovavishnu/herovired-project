class Car: # creating  class
    attr1="Audi"
    attr2="Benz"
    
    def names(self): #creating function
        print("The car name is",self.attr1)
        print("The car name is",self.attr2)


MyCar=Car() #creating object--Mycar is object and car is class
print(MyCar.attr1)
MyCar.names()
