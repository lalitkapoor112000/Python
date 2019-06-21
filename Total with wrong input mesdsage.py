def total(*args):
    s=0
    if all([(type(arg)==int or type(arg)==float) for arg in args]):
        for n in args:
            s=s+n
        return s
    else:
        return "Wrong Input"


print(total(1,2,3,4,5,6,7))
