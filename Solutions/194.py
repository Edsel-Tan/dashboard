g2 = {0 : [1,6],
      1 : [0,2,5],
      2 : [1,3,5],
      3 : [2,6],
      4 : [1,2,5],
      5 : [4,6],
      6 : [0,3,5]}
g1 = {0 : [1,3,6],
      1 : [0,2,5],
      2 : [1,3,5],
      3 : [0,2,6],
      4 : [1,2,5],
      5 : [4,6],
      6 : [0,3,5]}

mod = 10**8
factorial = [1]
for i in range(1, 9):
    factorial.append(factorial[-1] * i)

def calculate(g, c):
    if c == 0:
        return [()]
    n = len(g)
    solutions = [(1,[0])]
    for i in range(1,n):
        newsolutions = []
        # print(solutions)
        for numberOfColours, sol in solutions:
            pos = set([x for x in range(min(c, numberOfColours+1))])
            for j in g[i]:
                if j < i:
                    try:
                        # print(sol, sol[j])
                        pos.remove(sol[j])
                    except:
                        pass
                else:
                    break
            for j in pos:
                s = sol.copy()
                s.append(j)
                newsolutions.append((max(numberOfColours, j+1), s))
        solutions = newsolutions
    return solutions


a = 25
b = 75
c = 1984

g1_sols = calculate(g1, c)
g2_sols = calculate(g2, c)
g1_base = 0
g2_base = 0
g1_add = 0
g2_add = 0

for x, y in g1_sols:
    add = 1
    base = 1
    for i in range(x):
        base *= c - i
    for i in range(x-2):
        add *= c - 2 - i
    g1_base += base
    g1_add += add

for x, y in g2_sols:
    add = 1
    base = 1
    for i in range(x):
        base *= c - i
    for i in range(x-2):
        add *= c - 2 - i
    g2_base += base
    g2_add += add

def memoize(f):
    cache = {}
    def g(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return g

@memoize
def N(a, b):
    if a == 1 and b == 0:
        return g1_base
    if a == 0 and b == 1:
        return g2_base
    if b == 0:
        return (g1_add * N(a-1, b)) % mod
    if a == 0:
        return (g2_add * N(a, b-1)) % mod
    return ((g1_add * N(a-1, b)) + (g2_add * N(a, b-1))) % mod

# print(g1_add, g2_add, g1_base)
print(N(a, b))



