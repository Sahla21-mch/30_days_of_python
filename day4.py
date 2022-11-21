#instances(inheritance)
#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname,self.lastname)

pe = Person("sahla","sandrine")
pe.printname()

#Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) 
#Use the Student class to create an object, and then execute the printname method:
pe = Person("sahla","sandra")
pe.printname()
#Add the __init__() function to the Student class:
    
