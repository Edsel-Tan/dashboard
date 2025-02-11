from prime import primes

n = 10000000
p = primes(n)
e = []
mod = 10**9+7

for i in p:
    j = n//i
    e.append(0)
    while j > 0:
        e[-1] += j
        j = j//i

def f(x):
    output = 1
    for i in x:
        output *= i+1
        output %= mod
    return (output - 1) % mod

ans = 0
for i in range(1, e[0]+1):
    while e[-1]//i == 0:
        e.pop()
    ans = (ans + f([j//i for j in e])) % mod
print(ans)
