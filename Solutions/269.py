n = 16

def process(state):
    states = []
    for i in range(10):
        s = [list(j) for j in state]
        for j in range(len(s[0])):
            s[1][j] -= i

        d = []
        for j in range(len(s[0])-1, -1, -1):
            if s[1][j] % s[0][j] != 0:
                d.append(j)
        
        for j in d:
            del s[0][j]
            del s[1][j]

        for j in range(len(s[0])):
            s[1][j] = -s[1][j] // s[0][j]

        states.append(tuple([tuple(j) for j in s]))
    return states

starting_states = {}
for i in range(1, 10):
    d = []
    v = []
    for j in range(1, 10):
        if i % j == 0:
            d.append(j)
            v.append(i//j)
    starting_states[(tuple(d), tuple(v))] = 1

s = starting_states
for i in range(n-1):
    ns = {}
    for j in s.keys():
        for k in process(j):
            if k in ns:
                ns[k] += s[j]
            else:
                ns[k] = s[j]
    s = ns

ans = 0
for i in s.keys():
    if 0 in i[1]:
        ans += s[i]

print(ans+10**(n-1))