def common(l,m):
    res=[]
    l.remove('q')
    m.remove('q')
    for i in range(len(l)):
        if l[i]==m[i]:
            res.append(l[i])
    return res


k=[]
p=[]
while 'q' not in k:
    k.append(input("Enter numbers of list 1 and enter q to stop:"))
while 'q' not in p:
    p.append(input("Enter numbers of list 2 and enter q to stop:"))
print(common(k,p))
