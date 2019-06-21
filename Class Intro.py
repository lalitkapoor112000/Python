class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def is18(self):
        return self.age>18
p1=Person('Lalit','Kapoor',19)
p2=Person('Sonu','Kapoor',18)
print(p1.first_name)
print(p1.full_name())
print(p2.full_name())
print(p1.is18())
