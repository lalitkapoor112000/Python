def listSquare(m):
    sq=[]
    m.remove('q')
    for i in m:
        sq.append(int(i)**2)
    return sq

l=[]
i=0
while 'q' not in l:
    l.append(input("Enter list elements and enter to stop:"))
print(listSquare(l))    
        
