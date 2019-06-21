def generate_even(n):
    for i in range(2,n+1,2):
        yield i

print(list(generate_even(20)))
