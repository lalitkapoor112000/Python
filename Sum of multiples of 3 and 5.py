def sum35(limit):
    res=0
    for i in range(0,limit+1):
        if i%3==0 or i%5==0:
           res=res+i
    return res

l=int(input("Enter the limit to find sum=  "))
rest=sum35(l)
print(f"Sum of multipes of 3 and 5 upto {l} is {rest}")
