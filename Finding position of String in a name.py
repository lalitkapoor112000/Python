def pos(l,key):
    for index,name in enumerate(l):
        if key==name:
            return index
        else:
            return -1

l=['Lalit','lalit']
print(pos(l,'lalit'))
