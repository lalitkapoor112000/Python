def multiply(*args):
    m=1
    for i in args:
        m*=i
    return m

n=int(input("Enter  a number upto which you want product:"))
l=[i for i in range(1,n+1)]
print(multiply(*l))
