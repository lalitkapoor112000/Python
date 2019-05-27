def showNumbers(limit):
 for i in range(limit):
     if i%2==0:
         print("{} EVEN".format(i))
     else:
         print(f"{i} ODD")

num=None
num=int(input("Enter a limit and enter zero to exit:"))
showNumbers(num)
