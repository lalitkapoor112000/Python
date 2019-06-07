def filter(m):
    m.remove('q')
    odd=[]
    even=[]
    for i in m:
        if int(i)%2==0:
          even.append(i)
        else:
          odd.append(i)
    m.clear()
    m.append(even)
    m.append(odd)
    return m

l=[]
while 'q' not in l:
    l.append(input("Enter list elements numbers and press q to exit:"))
print(filter(l))
