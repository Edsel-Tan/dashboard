import math
from decimal import Decimal, getcontext
getcontext().prec = 50


keykey = {}
cache = {}
def f(x):
    key = math.floor(Decimal(2)**Decimal(Decimal(30.403243784)-x**2))
    if key in cache.keys():
        # print("LOOP FOUND! =)")
        return cache[key]
    else:
        cache[key] = key * Decimal(10**-9)
        keykey[key] = math.floor(2**(Decimal(30.403243784)-cache[key]**2))
        return cache[key]

u = Decimal(-1)
for i in range(700):
    # print(u)
    u = f(u)

fkey = math.floor(2**(Decimal(30.403243784)-u**2))
loop = []
loop.append(fkey)
k = keykey[fkey]
while k != fkey:
    loop.append(k)
    k = keykey[k]
print("{:.9f}".format(cache[loop[0]] + cache[loop[1]]))