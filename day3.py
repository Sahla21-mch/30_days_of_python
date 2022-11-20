#object method:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello! i'm " + self.name)

p1 = Person("Sandrine", 18)
p1.myfunc()
#self parameter
class Person:
    def __init__(happy,Name,age):
        happy.Name = Name 
        happy.age= age 

    def func (abc):
        print("hello!" + abc.age)

p1 = Person("sandrine", 18)
p1.func()
#modifyiong object properties
p1.age = 19   