#object method:
from os import name
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello! my name is " + self.name)

p1 = Person("Sandrine", 18)
p1.myfunc()
#self parameter
class person:
    def __init__(happy,name,age):
        happy.name = name 
        happy.age= age 

    def func(abc):
        print("hello!" + abc.name)

    p1 = Person("sandrine", 18)
    p1.func()