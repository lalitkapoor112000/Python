def checkSpeed(n):
 if n<=70:
     print('OK')
 elif n>70:
     n=n-70
     n=n//5
     print(f"Demerit points={n}")
     if n>12:
         print('License Suspended')

speed=None
while speed!=0:
 speed=int(input("Enter the Speed of driver and press zero to exit:"))
 checkSpeed(speed)
