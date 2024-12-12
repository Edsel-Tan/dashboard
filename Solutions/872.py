s = 10**17
e = 9**17
d = s - e
ans = s

def ld(x):
    o = 1
    while o <= x:
        o *= 2
    return o//2

while d > 0:
    ans += e
    e += ld(d)
    d -= ld(d)
print(ans)