num=input("Enter a number:")
n=len(num)
num=int(num)
res=0
for i in range(n):
   rem=int(num%10)
   res+=rem
   num//=10
print(f"Sum={res}")
