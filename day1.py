#intro to python classes
class Employee:

    def __init__(self,firstN,secondN,salary,specification):
        self.firstN = firstN
        self.secondN = secondN
        self.salary = salary
        self.specification = specification

    def fullName(self):
        return "{} {}".format(self.firstN, self.secondN)

emp_1 = Employee('Sandrine','Nyuyki', 1200000, 'mananger')
#print(Employee.fullName(emp_1))
print(emp_1.fullName())


