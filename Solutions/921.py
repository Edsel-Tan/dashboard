# Solution from abcdefg3085
from field_extension import create_mod

mod = 398874989
k = (mod-1)//4-1
n = 1618034

fib = [0,1]
for i in range(n):
    fib.append((fib[-1] + fib[-2]) % k)

Qp = create_mod(5, mod)
q = Qp(2, 1)

ans = 0
for i in range(2, n+1):
    qi = q ** (pow(5, fib[i], mod-1))
    ans = (ans + pow(qi.a, 5, mod) + pow(qi.b, 5, mod)) % mod
print(ans)