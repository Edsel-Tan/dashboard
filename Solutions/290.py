def s(n):
    output = 0
    while n > 0:
        output += n % 10
        n = n // 10
    return output

state = {(0,0):1}

for i in range(18):
    newstate = {}
    for j in state:
        for k in range(10):
            ns = list(j)
            ns[1] += k - (k*137+ns[0]) % 10
            ns[0] = (k*137+ns[0]) // 10
            ns = tuple(ns)
            if ns in newstate:
                newstate[ns] += state[j]
            else:
                newstate[ns] = state[j]
    state = newstate

# print(state)
ans = 0
for ns in state:
    if -s(ns[0]) + ns[1] == 0:
        ans += state[ns]
print(ans)