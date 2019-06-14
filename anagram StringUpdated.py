def anagrams(s,r):
    if len(s)!=len(r):
        print("String length not equal!")
    else:
        s=s.sort()
        r=r.sort()
        if s==r:
            return 'Anagrams'
        else:
            return "Not Anagrams"

a,b=input("Enter two Strings seperated by comma(,) to check Anagram:").split(",")
print(anagrams(a,b))

