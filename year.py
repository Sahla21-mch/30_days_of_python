class Student(Person):
    def __init__(self, firsname, lastname, year):
        super().__init__(firsname, lastname)
        self.graduationyear = year
#Use the Student class to create an object, and then execute the printname method:
pe = Person("sahla", "sandra" ,2025)
pe.printname()