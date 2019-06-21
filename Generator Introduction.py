def nums(n):
    for i in range(1,n+1):
        yield i

print(list(nums(10)))
