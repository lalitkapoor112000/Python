l1=[1,3,5,7]
l2=[2,4,6,8]
n=[]
for pair in zip(l1,l2):
    n.append(max(pair))
print(n)
