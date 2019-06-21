numbers=[i for i in range(17)]
def squares(a):
    return a**2

print(list(map(squares,numbers)))
print(type(map(squares,numbers)))
