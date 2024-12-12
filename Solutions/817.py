import math

def base(a,b):
    if a == 0:
        return [0]
    output = []
    c = int(math.log(a,b))
    e = c
    while a > 0:
        d = int(a / b ** c)
        output.append(d)
        a -= d * b**c
        c -= 1
    if len(output) < e + 1:
        output.append(0)
    return output

p = 10**9+7
p1 = math.isqrt(p) + 1
x = 10**5
p2 = math.isqrt( (p - x)*p )

d = {}

for i in range(1,int(p/2)+1):
    a = base(i**2,p)[-1]
    if a not in d.keys() and a >= p - x:
        d[a] = i

c = 0
p2 = math.isqrt((p - x)*p + c*p**2) - 1
while len(list(d.keys())) < 10 ** 5 and c<p:
    for i in range(p2, p2+x):
        a = base(i**2,p)[-2]
        if a < p/4:
            break
        if a not in d.keys() and a >= p - x:
            d[a] = i
        elif a in d.keys():
            if i < d[a]:
                d[a] = i
                
    c += 1
    p2 = math.isqrt((p - x)*p + c*p**2)

for i in range(p-x, p):
    if math.isqrt(i * p**2) + 1 < d[i]:
        d[i] = math.isqrt(i * p**2) + 1


t = 0
for i in d.keys():
    t += d[i]
print(t)