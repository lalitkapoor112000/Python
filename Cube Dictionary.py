def cubeDict(m):
    cubes={}
    for i in range(1,m+1):
        cubes[i]=i**3
    return cubes

num=input("Enter a number to create cub list:")
print(cubeDict(int(num)))

