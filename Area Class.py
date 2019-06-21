class Circle:
    count_instance=0
    pi=3.14142
    def __init__(self,radius):
        self.radius=radius
        Circle.count_instance+=1

    def area(self):
        return Circle.pi*(self.radius**2)

c1=Circle(5)
c2=Circle(10)
print(f"Area of circle ={c1.area()}")
print(f"No. of instances={Circle.count_instance}")
