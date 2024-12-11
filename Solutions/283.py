# abc = 4k**2 * (a+b+c), k <= 1000
# (ab - 4k**2)(ac - 4k**2) = 4k**2 * a**2 + 16k**4

kmax = 1000
n = (4*kmax) * (4*kmax) + 16 * kmax * kmax

pf = [[] for _ in range(n+1)]
for i in range(2, n+1):
    if len(pf[i]) == 0:
        for k in range(i, n+1, i):
            pf[k].append(i)
            pf[k].append(1)
        j = i * i
        while j <= n:
            for k in range(j, n+1, j):
                pf[k][-1] += 1
            j = i * j

def f(factors):
    output = [1]
    for i in factors:
        noutput = []
        c = 1
        for j in range(factors[i]+1):
            for k in output:
                noutput.append(c * k)
            c *= i
        output = noutput
    return sorted(output)

ans = 0
for k in range(1, kmax+1):
    for a in range(1, 4*kmax+1):
        factors = {2:2}
        for i in range(0, len(pf[k]), 2):
            x = pf[k][i]
            y = pf[k][i+1]
            if x in factors:
                factors[x] += y * 2
            else:
                factors[x] = y * 2
        z = a**2 + 4*k**2
        for i in range(0, len(pf[z]), 2):
            x = pf[z][i]
            y = pf[z][i+1]
            if x in factors:
                factors[x] += y
            else:
                factors[x] = y
        
        d = 4*k**2*a**2 + 16*k**4
        e = 4*k**2
        for i in sorted(f(factors)):
            x = i
            y = d//x
            if y < x:
                break
            if (y+e)%a == 0 and (x+e)%a == 0:
                b = (x+e)//a
                c = (y+e)//a
                if c >= b and b >= a:
                    ans += 2*(a+b+c)
            # x = -i
            # y = d//x
            # if (y+e)%a == 0 and (x+e)%a == 0:
            #     b = (x+e)//a
            #     c = (y+e)//a
            #     if c >= b and b >= a:
            #         ans += 2*(a+b+c)

print(ans)