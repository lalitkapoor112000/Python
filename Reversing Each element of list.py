def rev(m):
    m.remove('q')
    res=[]
    for i in m:
        i=i[::-1]
        res.append(i)
    return res

l=[]
while 'q' not in l:
    l.append(input("Enter elements(words) of the list and enter q to stop:"))
print(rev(l))
