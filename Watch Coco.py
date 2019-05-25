name,age=input("Enter your name and age sepeated by comma:").split(",")
age=int(age)
name=name.lower()
if name[0]=='a' and age>10:
    print("You can watch Coco movie:")
else:
    print("You cannot watch movie Coco:")
