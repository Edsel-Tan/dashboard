n,k = 1000000,20000
# from math import log, exp
import decimal #type: ignore
from decimal import Decimal #type: ignore
decimal.getcontext().prec = 50
log = Decimal.ln
exp = Decimal.exp

lf = []
lf.append(Decimal(0))
for i in range(1, n+1):
    lf.append(lf[-1] + log(Decimal(i)))

def lc(n, r):
    return lf[n] - lf[r] - lf[n-r]

ans = Decimal(0)
for a in range(k//2+1):
    b = k-2*a
    ans += exp(lc(n, a) + lc(n-a, b) + lf[k] - a * log(Decimal(2)) - k * log(Decimal(n)))
print("{:.10f}".format(1-ans))