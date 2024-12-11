import math
import itertools

p = 1009
q = 3643

# 1008 = 9 * 16 * 7
# 3642 = 2 * 3 * 607

def product(lis):
    output = 1
    for i in lis:
        output *= i
    return output

fac_p = [product(i) for i in itertools.product([1,2,4,8,16], [1,3,9],[1,7])]
fac_p = sorted(fac_p)
fac_q = [product(i) for i in itertools.product([1,2], [1,3],[1,607])]
fac_q = sorted(fac_q)
# fac_p = [product(i) for i in itertools.product([1,2], [1,3,9])]
# fac_p = sorted(fac_p)
# fac_q = [product(i) for i in itertools.product([1,2,4], [1,3,9])]
# fac_q = sorted(fac_q)

order_p = [1]
for i in range(1,p):
    for j in fac_p:
        if pow(i, j, p) == 1:
            order_p.append(j)
            break

order_q = [1]
for i in range(1,q):
    for j in fac_q:
        if pow(i, j, q) == 1:
            order_q.append(j)
            break

totient = (p-1) * (q-1)
sol = {}
for i in range(2, totient):
    if math.gcd(i, totient) == 1:
        sol[i] = 0

for m in range(p*q):
    e_min = math.lcm(order_p[m%p], order_q[m%q])
    # print(m, e_min)
    for j in range(e_min, totient, e_min):
        if j + 1 in sol:
            sol[j + 1] += 1

# print(sol, p*q, totient)

m = min(sol.values())
ans = 0
for i in sol.keys():
    if sol[i] == m:
        ans += i
print(ans)