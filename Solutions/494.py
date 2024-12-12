"""
Ideas: f(n) ~ F(n) where F(n) is the fibonacci sequence.
Consider starting at a power of 2 and generating a prefix p(n),
we have functions a(x) -> 2x and b(x) -> 2(x-1)/3 (3x+1 is even)
the composition of a and b leads to a prefix sequence. n integer implies
our starting point is some residue mod 3**k where k is the number of b operation

f(n) > F(n) when g(x) - x = 0 has solution x > 0 where g is a composition of
a and b. We also need that the "start point" is less than this solution x



"""
from fractions import Fraction
import math
import time

#Empirical evidence

MAX = 10**6
##SUPER FUCKING DUBIOUS LIMIT

def collatz(x):
    if x%2 == 0:
        return x//2
    else:
        return 3*x+1

def ispoweroftwo(x):
    return x&(x-1) == 0


collatz_cache = {}
collatz_min = {}

def collatz_seq(x):
    if ispoweroftwo(x):
        collatz_cache[x] = x
        return x
    if x in collatz_cache.keys():
        return collatz_cache[x]
    else:
        collatz_cache[x] = collatz_seq(collatz(x))
        if collatz_cache[x] not in collatz_min.keys():
            collatz_min[collatz_cache[x]] = x
        elif x < collatz_min[collatz_cache[x]]:
            collatz_min[collatz_cache[x]] = x
        return collatz_cache[x]


class LE:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        return LE(self.a * other.a, other.b * self.a + self.b)

    def __sub__(self,other):
        return LE(self.a - other.a, self.b - other.b)

    def __str__(self):
        return str(self.a) + "x " + str(self.b)

    def solve(self):
        return -self.b/self.a

G = LE(2,0)
F = LE(Fraction(1,3), Fraction(-1,3))


def check(SS, n):
    for j in SS[:-1]:
        if (SS[-1] - j).solve() > n:
            return True
    return False
            

seeds = [ (2**i-1)//3 for i in range(4,22,2)]
ss = 0
specSeq = []

for seed in seeds:
    if seed%3 == 0:
        continue
    posSeq = [[seed, LE(1,0)]]
    lt = time.time()
    while len(posSeq[0]) < 91:
        newPosSeq = []
        lt = time.time()
        for s in posSeq:
            
            if s[0] * 2 < MAX:
                seq = s.copy()
                seq[0] = 2 * seq[0]
                seq.append(G * seq[-1])
                if check(seq[1:], seed):
                    specSeq.append(seq)
                else:
                    newPosSeq.append(seq)

            
            if s[0] % 3 == 1 and s[0] % 2 != 1:
                seq = s.copy()
                seq[0] = (seq[0] - 1)//3
                seq.append(F * seq[-1])
                if check(seq[1:], seed):
                    specSeq.append(seq)
                else:
                    newPosSeq.append(seq)

        posSeq = newPosSeq
        if len(newPosSeq) == 0:
            break

del posSeq
for seq in specSeq:
    seqs = [seq[0]]
    counter = len(seq) - 1
    while counter < 90:
        counter += 1
        newseqs = []
        for s in seqs:
            if s % 2 != 1 and s % 3 == 1:
                newseqs.append((s*2))
                newseqs.append((s-1)//3)
            else:
                newseqs.append(s*2)
        seqs = newseqs.copy()
    ss += len(seqs)

s = [1,1,1]
for i in range(90):
    t = 0
    for i in range(len(s)-1):
        t += s[i]
    s.append(t)
print(ss + s[90])
            


