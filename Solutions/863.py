
tolerance = 100

def E(n):
    s = [0 for i in range(n)]

    for i in range(tolerance):
        ns = [0 for i in range(n)]
        for j in range(1, n):
            ns[j] = 1 + min(s[(5*j)%n] * ((5*j)%n) / (5*j), s[(6*j)%n] * ((6*j)%n) / (6*j))
        s = ns
    
    return s[1]


# print(E(8))
ans = 0
for i in range(2, 1001):
    ans += E(i)
print("{:.6f}".format(ans))