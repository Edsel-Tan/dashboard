from math import lcm
from prime import primes
# p = primes(100000)

total = 0
total2 = 0
v = []

p = [708*730, 509173, 1427*11, 17*41*719]
for t in p:
    # print(t)

    def rotate(s):
        output = []
        for i in range(len(s)):
            z = [s[(j+i)%len(s)] for j in range(len(s))]
            output.append(z)
        return output

    data = {}

    for h in range(t):
        s = (h * 720) % t
        m = (h * 12) % t
        pos = sorted([s,m,h])
        s,m,h = pos
        key = min(rotate((m-s, h-m, t-(h-s))))
        key = tuple(key[:2])
        if key in data:
            data[key] += 1
        else:
            data[key] = 1

    ans = 0
    tans = 0
    for i in data:
        if data[i] > 1:
            ans += data[i]
            tans += 1
    # print(ans, tans)
    total += ans
    total2 += tans
    if ans > 0:
        v.append(t)

print(total)
