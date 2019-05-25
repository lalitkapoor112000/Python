num=input("Enter a number:")
n=len(num)
i=0
res=0
while i<n:
    res+=int(num[i])
    i+=1
print(f"Sum={res}")   
