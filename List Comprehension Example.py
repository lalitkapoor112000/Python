l=[]
while 'q' not in l:
    l.append(input("Enter string to list and enter q to exit:"))
l.remove("q")
l=[i[::-1] for i in l]
print(l)
