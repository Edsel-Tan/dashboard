n = 40

def expand(state):
    ns = state[0]
    s = dict(*state[1:])
    output = {}
    for i in s.keys():
        for j in range(i):
            t = s.copy()
            t[i] -= 1
            if j in t:
                t[j] += 1
            else:
                t[j] = 1

            if i-1-j in t:
                t[i-1-j] += 1
            else:
                t[i-1-j] = 1

            if 0 in t:
                del t[0]
            if t[i] == 0:
                del t[i]

            nt = max(sum(t.values()), ns)
            key = (nt, tuple(sorted(t.items())))
            if key in output:
                output[key] += s[i]
            else:
                output[key] = s[i]

    return output

states = {(1, ((n, 1),)) : 1}

for i in range(n):
    nstates = {}
    for j in states.keys():
        x = expand(j)
        for k in x.keys():
            if k in nstates:
                nstates[k] += states[j] * x[k]
            else:
                nstates[k] = states[j] * x[k]
    states = nstates
ans = 0
for i in states:
    ans += states[i] * i[0]
import math
print("{:.6f}".format(ans/math.factorial(n)))



