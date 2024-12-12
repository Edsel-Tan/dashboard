class UnionFind:

    def __init__(self, n):
        self.ptr = [i for i in range(n)]

    def find(self, x):
        if self.ptr[x] == x:
            return x
        self.ptr[x] = self.find(self.ptr[x])
        return self.ptr[x]
    
    def union(self, x, y):
        self.ptr[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    

from prime import primes
n = 10**7
p = set(primes(n))

def edges(x, n):
    output = []

    s = str(x)
    if len(s) > 1 and s[1] != '0':
        if int(s[1:]) in p:
            output.append(int(s[1:]))
    
    y = 0
    c = 1
    while x > 0:
        z = x%10
        for i in range(1 if x < 10 else 0, 10):
            w = (x - z + i) * c + y
            if w in p and w <= n:
                output.append(w)
        y += z*c
        c *= 10
        x = x//10
    return output

ans = 0
uf = UnionFind(n+1)
for i in p:
    for j in edges(i, i):
        uf.union(i, j)
    if not uf.connected(2, i):
        ans += i


print(ans)