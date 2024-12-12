n = 10**16
m = 7**10
fibs = [[0,1,1,1]]

while fibs[-1][2] + fibs[-1][3] < n:
    v = [fibs[-1][0] + fibs[-1][2],
                 fibs[-1][1] + fibs[-1][3],
                 fibs[-1][0] + 2*fibs[-1][2],
                 fibs[-1][1] + 2*fibs[-1][3]
                 ]
    # v.append(fibs[-1][4] + v[0] + v[2])
    # v.append(fibs[-1][5] + v[1] + v[3])
    fibs.append(v)
del fibs[-1]

t = lambda x: ((x*(x+1))//2)%m
s = lambda x: ((x*(x+1)*(2*x+1))//6)%m

def f(x, y, p, q):
    output = 0
    output += t(n//x)*p
    for a in range(1, y+1):
        z = (n-a*x)//y
        if z <= 0:
            break
        l = z // x
        output += (l+1)*a*z*p
        output += y*z*t(l)*p
        output -= x*y*s(l)*p
        output -= a*x*t(l)*p

    for k in range(1, x+1):
        z = (n-y*k)//x
        if z <= 0:
            break
        l = z//y
        output += (l+1)*k*z*q
        output += x*z*t(l)*q
        output -= x*y*s(l)*q
        output -= k*y*t(l)*q

    return output % m

ans = 0

for i in fibs:
    ans += f(i[2] + 2*i[3], i[3], i[0] + i[2] + 2*i[1] + 2*i[3], i[1] + i[3])
    ans = ans % m

print(ans%m)


