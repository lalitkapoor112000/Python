d={i:'even' if i%2==0 else 'odd' for i in range(10)}
print(d)
for k,v in d.items():
    print(f"{k} is {v}")
