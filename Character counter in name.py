name=input("Enter your name:")
n=len(name)
i=0
temp=""
while i<n:
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]}={name.count(name[i])}")
    i+=1
