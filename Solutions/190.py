from decimal import * # type: ignore
import math

getcontext().prec = 50

def S(m):

    output = Decimal(1)
    for i in range(1,m+1):
        output *= (Decimal(i)*Decimal(2)/Decimal(m+1))**i
    return output

ans = 0
for i in range(2,16):
    ans += math.floor(S(i))
print(ans)
