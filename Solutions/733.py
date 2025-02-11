mod = 10**9+7

from segmenttree import FastSegmentTree as SegmentTree


n = 10**6
a = [153]

for i in range(n-1):
    a.append((a[-1] * a[0]) % 10000019)

keys = sorted(set(a))
idx = {}
for i in range(len(keys)):
    idx[keys[i]] = i

s = [SegmentTree(len(keys), 0, lambda x,y : (x+y)%mod) for i in range(4)]
c = [SegmentTree(len(keys), 0, lambda x,y : (x+y)%mod) for i in range(4)]

s : list[SegmentTree]
c : list[SegmentTree]


for i in range(n):
    v = a[i]
    key = idx[v]
    
    s[0].update(key, v)
    c[0].update(key, 1)

    for i in range(1, 4):
        s[i].update(key, s[i-1].query(0, key))
        s[i].update(key, c[i-1].query(0, key) * v)
        c[i].update(key, c[i-1].query(0, key))

print(s[3].query(0, len(keys)))