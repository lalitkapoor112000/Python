def pattern(m,n):
    for i in range(1,m+2):
        for j in range(1,i):
            print(j,end=" ")
        print("\n")

r,c=input("Enter row and column seperated by comma:").split(",")
pattern(int(r),int(c))
