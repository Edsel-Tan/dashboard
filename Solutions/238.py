s0 = 14025256
m = 20300713
v = set()
v.add(s0)

def dappend(a, x):
    t = []
    while x > 0:
        t.append(x%10)
        x = x//10
    for i in t[::-1]:
        a.append(i)
        

f = lambda x : (x**2) % m
s = f(s0)
r = []
dappend(r, s0)
while s not in v:
    dappend(r, s)
    v.add(s)
    s = f(s)

def dsum(x):
    output = 0 
    while x > 0:
        output += x % 10
        x = x//10
    return output

s = 0
for i in v:
    s += dsum(i)

m = [0 for i in range(s)]
m[0] = 1
a = set([i for i in range(s)])
a.remove(0)

for i in range(100):
    c = 0
    for j in range(i, len(r)+i):
        c += r[j%(len(r))]
        if c in a:
            a.remove(c)
            m[c] = i+1

n = 1000

n = 2*10**15
print(sum(m) * (n//s) + sum(m[1:(n%s)+1]))



