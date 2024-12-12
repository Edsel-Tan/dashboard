import math
from decimal import *
getcontext().prec = 30

k = 10**16
n = 10**4

numbers = [i for i in range(2,n+1)]
twologten = Decimal(2).log10()
lognumbers = [(Decimal(i).log10().log10())/twologten for i in range(2,n+1)]
lognumbers.insert(0,0)
lognumbers.insert(0,0)

def f(k,a,b):
    return min(math.ceil(k + lognumbers[a] -lognumbers[b]), 0)

summ = sum(lognumbers)
output = {}
for i in range(2, n+1):
    
    output[i] = math.floor((k + summ)/(n-1) - lognumbers[i])
    
    lognumbers[i] += output[i]


while sum(output.values()) < k:
    minn = (k, 0)
    for i in range(2,n+1):
        if lognumbers[i] <= minn[0]:
            minn = (lognumbers[i], i)
    output[minn[1]] += 1
    lognumbers[minn[1]] += 1

ans = 0
for i in range(2, n+1):
    ans = (ans + pow(i, pow(2, output[i], 1234567890), 1234567891))%1234567891
print(ans)
