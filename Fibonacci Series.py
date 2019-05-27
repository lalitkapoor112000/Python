def fibonacci(n):
 a=0
 b=1
 c=0
 while c<n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c

num=int(input("Enter a number to print fibonacci series:"))
fibonacci(num)
