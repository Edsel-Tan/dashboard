from prime import primes
mod = 10**18

class SegmentTree:

    def __init__ (self, l, r):
        self.l = l
        self.r = r
        self.v = 0
        self.lt = None
        self.rt = None
        if (r-l >= 1):
            m = (r+l)//2
            self.lt = SegmentTree(l,m)
            self.rt = SegmentTree(m+1,r)

    def add(self, l, r, x):
        if self.r < l:
            return
        if self.l > r:
            return
        if self.l >= l and self.r <= r:
            self.v += x
            self.v = self.v % mod
        else:
            self.lt.add(l, r, x)
            self.rt.add(l, r, x)
        return

    def query(self, x):
        if x >= self.l and x <= self.r:
            if self.r == self.l:
                return self.v
            else:
                return (self.v + self.lt.query(x) + self.rt.query(x))%mod
            
        return 0


n = 60 * 10**6
t = [1 for i in range(n+2)]
p = primes(n+3)

j = 4
e = 1
while j < n+2:
    for k in range(j, n+2, j):
        t[k] *= e+1
        t[k] //= e
        
    j *= 2
    e += 1

for i in p[1:]:
    j = i
    e = 1
    while j < n+2:
        for k in range(j, n+2, j):
            t[k] *= e+1
            t[k] //= e
            
        j *= i
        e += 1

u = []
for i in range(1, n+1):
    u.append(-t[i]*t[i+1])
    
a = sorted(set(u))
b = [i for i in range(len(a))]
c = dict(zip(a,b))
u = [c[i] for i in u]

l = len(a)

singlecount = SegmentTree(0, l-1)
paircount = SegmentTree(0, l-1)

ans = 0
c = 0
for i in u:
    singlecount.add(i+1, l-1, 1)
    v = singlecount.query(i)
    paircount.add(i+1, l-1, v)
    ans += paircount.query(i)

print(ans%(10**18))


