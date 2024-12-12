from math import gcd
from prime import memoize

n = 34
p = 83456729

s = [[] for i in range(n+1)]
for i in range(2, n+1):
    for j in range(i+1, n+1, 2):
        if (gcd(i,j) == 1):
            s[i].append(j)
            s[j].append(i)

for i in range(len(s)):
    s[i] = tuple(s[i])

c = {}
for i in range(2, n+1):
    if s[i] not in c:
        c[s[i]] = len(c)

d = [0 for i in c]
for i in c:
    d[c[i]] = set([c[s[j]] for j in i])


cache = {}

# @memoize
def f(state, x):
    if (state, x) in cache:
        return cache[(state, x)]
    
    if sum(state) == 0:
        return 1
    
    ans = 0
    for i in d[x]:
        if state[i] > 0:
            ns = list(state)
            ns[i] -= 1
            ans += f(tuple(ns), i) * state[i]
            ans %= p
    
    cache[(state, x)] = ans%p
    return ans%p

starting_state = [0 for i in c]
for i in range(2, n+1):
    starting_state[c[s[i]]] += 1
starting_state = tuple(starting_state)

# print(starting_state)

rough = 1
for i in starting_state:
    rough *= i+1

ans = 0
for i in range(2, n+1, 2):
    ns = list(starting_state)
    ns[c[s[i]]] -= 1
    ans += f(tuple(ns), c[s[i]])
    ans %= p

print(ans, len(cache))