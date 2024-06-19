
x = 0
sol = set()
while True:
    x += 1
    y = x**3+x+1
    p = 3
    while y > 1:
        if y%p==0:
            sol.add((p,x%p))
        while y%p==0:
            y//=p
        p+=2
    print(sorted(sol))
