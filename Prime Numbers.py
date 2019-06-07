def prime(limit):
    k=0
    for i in range(1,limit+1):
          k=0    
          for m in range(1,i+1):
              if i%m==0:
                  k+=1
          if k==2:
              print(m)

num=int(input("Enter a limit to print primt numbers:"))
prime(num)
