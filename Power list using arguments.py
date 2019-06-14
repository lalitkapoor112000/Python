def power(n,*args):
    if args:
       return [i**n for i in args]
    else:
        return 'You did not pass any args'

num=int(input("Enter the power:"))
m=int(input("Enter list limit:"))
k=[i for i in range(1,m+1)]
print(k)
print(power(num,*k))
