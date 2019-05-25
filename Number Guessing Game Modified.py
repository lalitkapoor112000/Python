import random
num=random.randint(1,101)
x=int(input("Guess a number:"))
k=0
while x!=num:
    if x>num:
        print("Too high")
    else:
        print("Too Low")
    x=int(input("Guess again:"))
    k+=1
print(f"You Won,in {k} times")
