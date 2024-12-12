from prime import miller_rabin, memoize

mod = 912491249

@memoize
def g(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    
    s = set()
    for x in [1,2,4,9]:
        s.add(g(n-x))
    for x in range(1,n):
        s.add(g(x) ^ g(n-x))
    
    y = 0
    while y in s:
        y += 1
    return y

start = 332
cycle = 11060

n = 12491249
k = 1249
residues = 11

s = [set() for i in range(residues)]
for i in range(1,start):
    if i > n:
        break
    s[g(i)].add(i)

for i in range(start, start+cycle):
    if i > n:
        break
    j = g(i)
    while i not in s[j] and i <= n:
        s[j].add(i)
        i += cycle


f = []
fi = []
f.append(1)
fi.append(1)
for i in range(1,n):
    f.append((f[-1] * i)%mod)
    fi.append(pow(f[-1], -1, mod))

def c(n, r):
    if n < 0 or r < 0 or r > n:
        return 0
    return ((f[n] * fi[n-r])%mod * fi[r])%mod

@memoize
def h(x, y, z):
    if x == 0 and z == 0:
        return 1
    if x == 0 and z != 0:
        return 0
    if y < 0:
        return 0
    
    ans = 0
    ans += h(x,y-1,z)
    for i in range(1,x+1):
        ans += h(x-i, y-1, z ^ (i%2 * y)) * c(len(s[y])+i-1, len(s[y])-1)
        ans %= mod

    return ans

print(h(k, residues-1, 0)%mod)
# print(2259208528408%mod)