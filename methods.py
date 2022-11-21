class Person:
    def __init__(self,firstname,lastname,year):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
    def printname(self):
        print(self.firstname,self.lastname,self.year)

pe = Person("sahla","sandrine",2025)
pe.printname()

#Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
    def __init__(self, firsname, lastname, year):
        super().__init__(firsname, lastname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

    
#Use the Student class to create an object, and then execute the printname method:
pe = Person("sahla", "sandra","2023")
pe.printname()
#Add the __init__() function to the Student class:
    
