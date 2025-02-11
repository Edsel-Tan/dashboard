m, w = 8, 64
mod = 10**9 + 7

states = {}
h = pow(2, -1, mod)

for a in range(1, w):
    for b in range(1, w-a):
        for c in range(1, w-a-b+1):
            state = (abs(a-b), c-1)
            if state not in states:
                states[state] = 0
            states[state] += 1

for i in range(3):
    nstates = {}
    for j in states:
        for k in states:
            state = (j[0] + k[0], j[1] ^ k[1])
            if state not in nstates:
                nstates[state] = 0
            nstates[state] = (nstates[state] + states[j] * states[k] * h) % mod
            state = (abs(j[0] - k[0]), j[1] ^ k[1])
            if state not in nstates:
                nstates[state] = 0
            nstates[state] = (nstates[state] + states[j] * states[k] * h) % mod
    states = nstates

ans = 0
for i in states:
    if i[0] == 0 and i[1] > 0:
        ans = (ans + states[i]) % mod
    elif i[0] > 0:
        ans = (ans + states[i] * h) % mod
print(ans)
