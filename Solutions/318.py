from math import sqrt, log10, ceil

ans = 0
t = 10**6
target = 2011


for p in range(1, 2012):
    for q in range(p+1, 2012-p):
        d = sqrt(q) - sqrt(p)
        if d >= 1:
            break
        ans += ceil(target/(-log10(d))/2)

print(ans)