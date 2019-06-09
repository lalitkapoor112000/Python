def wordCount(s):
    count={}
    for c in s:
        count[c]=s.count(c)
    return count

n=input("Enter any word to count words:")
print(wordCount(n))
