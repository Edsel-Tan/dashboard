from prime import primes
import math
import itertools

n = 800
p = primes(n+1)
p_sqrt = primes(math.isqrt(n)+1)
mod = 10**9 + 7
for i in p_sqrt:
    p.remove(i)

# print(p, p_sqrt)

exp = []
for i in p_sqrt:
    exp.append(math.floor(math.log(n, i)))

def product(lis):
    output = 1
    for i in range(len(lis)):
        output *= p_sqrt[i] ** lis[i]
    return output

factors = []
for i in itertools.product(*[range(i+1) for i in exp]):
    factors.append(product(i))
factors = sorted(factors)
# print(factors[:100])

count = dict(zip(factors, [0 for i in factors]))
count[1] = 1

def important(m):
    for i in p_sqrt:
        while m % i == 0:
            m = m // i
    return m == 1

for i in range(1, n+1):
    if important(i):
        newcount = count.copy()
        for c in count.keys():
            newcount[math.lcm(c, i)] += count[c]
            newcount[math.lcm(c, i)] = newcount[math.lcm(c, i)] % mod
        count = newcount

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
def S(n):
    output = {}
    c = []
    for i in p_sqrt:
        c.append(math.floor(math.log(n, i)))
    for i in itertools.product(*[range(i+1) for i in c]):
        output[product(i)] = 0
    output[1] = 1
    for i in range(1,n+1):
        newoutput = output.copy()
        for j in output.keys():
            newoutput[math.lcm(j, i)] += output[j] 
            newoutput[math.lcm(j, i)] = newoutput[math.lcm(j, i)] % mod
        output = newoutput
    output[1] -= 1
    return output



# print(S(4))

ans = {}
for i in count.keys():
    ans[i] = (count[i] * i) % mod

for j in p:
    print(j)
    newans = ans.copy()
    k = n//j
    s = S(k)
    # print("ans: ", ans, "\n S:", s, k)
    for i in s.keys():
        print(i)
        for k in ans.keys():
            f = math.lcm(k, i)
            newans[f] += ans[k] * s[i] * j * (f // k)
            newans[f] = newans[f] % mod
    ans = newans
            
# print(ans)
a = 0
for i in ans.keys():
    a += ans[i]
print(a)
# print(8463108648960)








