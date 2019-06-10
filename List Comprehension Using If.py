l=[]
while 'q' not in l:
    l.append(input("Enter numbers in list and hit q to stop:"))
l.remove('q')
l=[i for i in l if int(i)%2==0]
print(l)
