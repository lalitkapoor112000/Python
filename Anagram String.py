def anagrams(s,r):
    ss=[]
    rr=[]
    if len(s)!=len(r):
        print("String length not equal!")
    else:
        for i in range(0,len(s)):
            ss.append(s[i].lower())
            rr.append(r[i].lower())
        ss=ss.sort()
        rr=rr.sort()
        if ss==rr:
            return 'Anagrams'
        else:
            return "Not Anagrams"

a,b=input("Enter two Strings seperated by comma(,) to check Anagram:").split(",")
print(anagrams(a,b))

