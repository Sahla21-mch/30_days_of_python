#using the init function
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def __str__(self):
          return f"{self.name}({self.age})"
p1 = person('sandrine',18)
print(p1.name )
print(p1.age) 
print(p1)