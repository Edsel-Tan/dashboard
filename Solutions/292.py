import math

p = 120
hp = p//2
rtp = math.isqrt(p)
s = []

for m in range(1, rtp+1):
    for n in range(m+1, rtp+1, 2):
        if math.gcd(m, n) != 1:
            continue
        if m**2 + n**2 > hp:
            break
        s.append((n**2-m**2, 2*n*m, m**2+n**2))
        s.append((2*n*m, n**2-m**2, m**2+n**2))
        s.append((-2*n*m, n**2-m**2, m**2+n**2))
        s.append((m**2-n**2, 2*n*m, m**2+n**2))

s.append((1,0,1))
s.append((0,1,1))

states = {(0,0,0):1}
for i in s:
    nstates = {}
    for j in states.keys():
        for k in range((p-j[2])//i[2]+1):
            key = (j[0] + k*i[0], j[1] + k*i[1], j[2] + k*i[2])
            if key in nstates:
                nstates[key] += states[j]
            else:
                nstates[key] = states[j]
    states = nstates

pstates = {}
for i in states:
    j = (i[0],i[1])
    if j in pstates:
        if i[2] in pstates[j]:
            pstates[j][i[2]] += states[i]
        else:
            pstates[j][i[2]] = states[i]
    else:
        pstates[j] = {i[2] : states[i]}
# print(len(pstates))

ans = 0
for i in pstates.keys():
    for j in pstates[i].keys():
        for k in pstates[i].keys():
            if k + j <= p:
                ans += pstates[i][j] * pstates[i][k]


for i in s:
    ans -= hp//i[2]
ans -= 1

print(ans)