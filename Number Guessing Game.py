import random
n=random.randint(1,10)
x=input("Guess a number:")
x=int(x)
if x==n:
    print("You Win")
elif x<n:
    print("Too Low")
else:
    print("Too High")
