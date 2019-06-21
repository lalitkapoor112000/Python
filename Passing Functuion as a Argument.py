def square(n):
    return n**2
l=[1,2,3,4,5,6,7,8,9]

def my_fun(func,l):
    m=[func(i) for i in l]
    return m
print(my_fun(square,l))
