def revList(m):
    m.remove('q')
    res=[]
    for i in m[::-1]:
        res.append(i)
    return res

l=[]
while 'q' not in l:
    l.append(input("Enter List elements and enter q to stop:"))
print(revList(l))
