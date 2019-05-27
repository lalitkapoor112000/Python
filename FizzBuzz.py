def fizz_buzz(n):
 if n%3==0 and n%5==0:
     return 'FizzBuzz'
 elif n%3==0:
     return "Fizz"
 elif n%5==0:
     return 'Buzz'
 else:
     return n
    
num=None
while num!=0:
 num=int(input("Enter a number and enter zero to exit:"))
 print(fizz_buzz(num))
