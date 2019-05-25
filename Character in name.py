name,key=input("Enter your name and a character seperated by comma:").split(",")
print(f"Length of your name is {len(name.strip())}")
print(f"Hi {name} ,{key} is {name.lower().strip().count(key.lower().strip())} times in your name")
