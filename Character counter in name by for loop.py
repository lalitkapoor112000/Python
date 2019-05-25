name=input("Enter your name:")
l=len(name)
temp=""
for i in range(l):
    if name[i] not in temp:
       temp+=name[i]
       print(f"{name[i]}={name.count(name[i])} times")
