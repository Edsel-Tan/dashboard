from prime import primes
import math

n = 10**18
m = math.ceil((n//4)**(1/3))

p = primes(m)


stack = [[len(p)-1,1,0,1,0]]
ans = 0

while len(stack) > 0:

    t = stack[-1]
    del stack[-1]

    if t[0] < 0:
        if t[2] != 1 or t[4] != 1:
            continue

        ans += 1
        continue

    #All possible stuff
    pi = p[t[0]]
    pos = []
    pos.append(t.copy())
    s = t.copy()
    s[1] *= pi
    s[3] *= pi - 1

    while s[1] < n:
        pos.append(s.copy())
        s[1] *= pi
        s[3] *= pi

    for s in pos:
        #Check
        a = 0
        b = 0
        c = s[1]
        d = s[3]

        while c % pi == 0:
            a += 1
            c //= pi
        while d % pi == 0:
            b += 1
            d //= pi

        if a == 1 or b == 1:
            continue

        s[0] -= 1
        s[2] = math.gcd(s[2], a)
        s[4] = math.gcd(s[4], b)
        stack.append(s)

print(ans)

