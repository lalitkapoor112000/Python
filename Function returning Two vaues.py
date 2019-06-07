def two(m,n):
    mult=m*n
    add=m+n
    return mult,add

num1=int(input('Enter number A:'))
num2=int(input('Enter number B:'))
m,a=two(num1,num2)
print(f"Product ={m}")
print(f"Sum={a}")
