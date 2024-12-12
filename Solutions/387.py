from prime import miller_rabin

ans = 0

solutions = [(i,i) for i in range(1,10)]
strong = []

for i in range(13):
    ns = []
    s = []

    for j in solutions:
        for k in range(10):
            x = j[0] * 10 + k
            y = j[1] + k
            if x%y == 0:
                if miller_rabin(x//y):
                    s.append((x,y))
                else:
                    ns.append((x,y))

    for j in strong:
        for k in range(10):
            x = j[0] * 10 + k
            y = j[1] + k
            if miller_rabin(x):
                ans += x

            if x%y == 0:
                if miller_rabin(x//y):
                    s.append((x,y))
                else:
                    ns.append((x,y))

    solutions = ns
    strong = s

print(ans)
