def reverseList(m):
    m.remove('q')
    res=m[::-1]
    return res

m=[]
while 'q' not in m:
    m.append(input("Enter List elements and enter q to stop:"))
print(reverseList(m))
