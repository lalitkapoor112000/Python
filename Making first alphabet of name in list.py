def titleName(*args):
        l=[i.title() for i in args]
        return l

m=[input("Enter names in List:") ]
print(titleName(*m))
    
        
