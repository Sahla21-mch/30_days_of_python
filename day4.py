#instances(inheritance)
#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self,firstname,lastname,year):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
    def printname(self):
        print(self.firstname,self.lastname,self)

pe = Person("sahla","sandrine",)
pe.printname()

#Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
    def __init__(self, firsname, lastname ):
        super().__init__(firsname, lastname)
        
    
#Use the Student class to create an object, and then execute the printname method:
pe = Person("sahla", "sandra",)
pe.printname()
#Add the __init__() function to the Student class:
    
