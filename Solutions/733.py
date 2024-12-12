mod = 10**9+7

class SegmentTree:
    
    def __init__(self, x, y, f = lambda x, y: x + y):
        self.left: SegmentTree
        self.right: SegmentTree

        self.value = 0
        self.left = None
        self.right = None
        self.l = x
        self.r = y
        self.f = f
        if y-x > 0:
            self.left = SegmentTree(x, (x+y)//2)
            self.right = SegmentTree((x+y)//2+1, y)
    
    def query(self, x, y):
        if x > self.r or y < self.l:
            return 0
        if x <= self.l and y >= self.r:
            return self.value
        return self.f(self.left.query(x, y), self.right.query(x, y))
    
    def update(self, x, v):
        if x > self.r or x < self.l:
            return
        if self.l == self.r and self.l == x:
            self.value = self.f(self.value, v)
            return
        self.value = self.f(self.value, v)
        self.left.update(x, v)
        self.right.update(x, v)


n = 10**6
a = [153]

for i in range(n-1):
    a.append((a[-1] * a[0]) % 10000019)

keys = sorted(set(a))
idx = {}
for i in range(len(keys)):
    idx[keys[i]] = i

s = [SegmentTree(0, len(keys), lambda x,y : (x+y)%mod) for i in range(4)]
c = [SegmentTree(0, len(keys), lambda x,y : (x+y)%mod) for i in range(4)]

s : list[SegmentTree]
c : list[SegmentTree]


for i in range(n):
    v = a[i]
    key = idx[v]
    
    s[0].update(key, v)
    c[0].update(key, 1)

    for i in range(1, 4):
        s[i].update(key, s[i-1].query(0, key-1))
        s[i].update(key, c[i-1].query(0, key-1) * v)
        c[i].update(key, c[i-1].query(0, key-1))

print(s[3].query(0, len(keys)))