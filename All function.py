n1=[2,4,6,8,10]
n2=[1,3,5,7]
evens=[]
odds=[]
for num in n1:
    evens.append(num%2==0)
for i in n2:
    odds.append(i%2==0)
print(all(odds))
print(all(evens))
        
