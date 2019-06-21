def square(n):
    s=(i**2 for i in range(1,n+1))
    return s

for i in square(20):
    print(i)
