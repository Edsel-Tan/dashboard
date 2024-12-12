n = 10000

ans = 2
for x in range(3, n+1):

    states = {}
    for j in range(0, 3):
        states[j%x] = j
    
    m = 10
    f = True
    while f:
        ns = {}
        for j in range(1,3):
            for k in states:
                l = (j*m + k) % x
                if l == 0:
                    f = False
                    l = (j*m+states[k])
                    break
                if l not in states and l not in ns:
                    ns[l] = j*m + states[k]
            if not f:
                break

        for i in ns:
            states[i] = ns[i]

        m *= 10

    ans += (l // x)

print(ans)