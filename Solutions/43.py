ans = 0
c = (2<<10)-1
s = ""

from prime import primes
p = primes(20)

def f():
    global ans, s, c
    if len(s) == 10:
        ans += int(s)
    if len(s) > 2:
        for i in range(10):
            if (c & (1 << i)):
                x = int(s[-2] + s[-1] + str(i))
                if x % p[len(s)-3] == 0:
                    s += str(i)
                    c -= (1 << i)
                    f()
                    c += (1 << i)
                    s = s[:-1]
    elif len(s) > 0:
        for i in range(10):
            if (c & (1 << i)):
                s += str(i)
                c -= (1 << i)
                f()
                c += (1 << i)
                s = s[:-1]
    else:
        for i in range(1,10):
            if (c & (1 << i)):
                s += str(i)
                c -= (1 << i)
                f()
                c += (1 << i)
                s = s[:-1]

f()
print(ans)