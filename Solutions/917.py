import sys
from math import inf
from itertools import accumulate
from collections import defaultdict
from segmenttree import FastSegmentTree as SegmentTree

INT_MAX = 10**9
MOD = 998388889
N = 10**7


def cost(sx, sy, ex, ey):
    if sx > ex or sy > ey:
        return inf
    if sx == ex:
        return (ey - sy + 1) * a[2 * sx] + (ay[ey + 1] - ay[sy])
    if sy == ey:
        return (ex - sx + 1) * a[2 * sy + 1] + (ax[ex + 1] - ax[sx])

    if (sx, sy, ex, ey) in vst3:
        return vst3[(sx, sy, ex, ey)]

    mx = tx.query(sx, ex + 1)
    my = ty.query(sy, ey + 1)
    mxi = key[mx] // 2
    myi = key[my] // 2

    v = min(cost(sx, sy, mxi - 1, myi), cost(sx, sy, mxi, myi - 1)) + \
        a[2 * mxi] + a[2 * myi + 1] + \
        min(cost(mxi + 1, myi, ex, ey), cost(mxi, myi + 1, ex, ey))

    vst3[(sx, sy, ex, ey)] = v
    return v


def est(sx, sy, ex, ey):
    if sx > ex or sy > ey:
        return
    if sx == ex or sy == ey:
        return

    mx = tx.query(sx, ex + 1)
    my = ty.query(sy, ey + 1)
    mxi = key[mx] // 2
    myi = key[my] // 2

    lx.add(mxi)
    ly.add(myi)

    if (sx, sy, ex, ey) in vst:
        return
    vst.add((sx, sy, ex, ey))

    est(sx, sy, mxi - 1, myi)
    est(sx, sy, mxi, myi - 1)
    est(mxi + 1, myi, ex, ey)
    est(mxi, myi + 1, ex, ey)


def m(x, y):
    return a[2 * x] + a[2 * y + 1]


a = [102022661]
for i in range(1, 2 * N):
    a.append((a[-1] * a[-1]) % MOD)

key = {a[i]: i for i in range(len(a))}
ax = list(accumulate(a[::2], initial=0))
ay = list(accumulate(a[1::2], initial=0))

tx = SegmentTree(N, INT_MAX, lambda x, y: min(x, y))
ty = SegmentTree(N, INT_MAX, lambda x, y: min(x, y))

for i in range(N):
    tx.update(i, a[2 * i])
    ty.update(i, a[2 * i + 1])

vst = set()
vst3 = {}
lx = set()
ly = set()

print(cost(0, 0, N - 1, N - 1))
