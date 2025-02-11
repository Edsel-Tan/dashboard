m, w = 8, 64
mod = 10**9+7

def convert(a, b, k):
    x, y = 0, a * k
    for i in range(k):
        if y > x and y <= x + b:
            return x+b-y, 0
        x += b
        if x < y and x > y - a:
            return 0, y - x
        if x == y-a:
            return a, b
        y -= a

states = {}
fixed_states = {}

for a in range(1, w):
    for b in range(1, w-a):
        for c in range(1, w-a-b+1):
            state = convert(a, b, c)
            if 0 in state:
                if state not in fixed_states:
                    fixed_states[state] = 0
                fixed_states[state] += 1
                continue
            if state not in states:
                states[state] = 0
            states[state] += 1

states_keys = sorted(states.keys(), key=lambda x: sum(x))
            #  (max(abs(x[0]), abs(x[1])),
            #   min(abs(x[0]), abs(x[1]))))

l = 20
f = [1]
fi = [1]
for i in range(1, l):
    f.append((f[-1] * i) % mod)
    fi.append(pow(f[-1], -1, mod))
def c(n, r):
    return (f[n] * fi[n-r] * fi[r]) % mod

dp = [[{} for j in range(m+1)] for i in range(len(states))]

for i in range(len(states)):
    dp[i][0][(0,0)] = 1

def add(x, y, z):
    a = z//2 + z%2
    b = z//2
    return (a * y[0] - b * y[1] + (x[1] if z % 2 == 1 else x[0]), 
            -a * y[1] + b * y[0] + (x[0] if z % 2 == 1 else x[1]))

for i in range(1, m+1):
    for j in dp[0][0]:
        s = states_keys[0]
        ns = add(j, s, i)
        if ns not in dp[0][i]:
            dp[0][i][ns] = 0
        dp[0][i][ns] = (dp[0][i][ns] + pow(states[s], i, mod)) % mod

for i in range(1, len(states)):
    for j in range(1, m+1):
        s = states_keys[i]
        for k in range(j+1):
            for l in dp[i-1][j-k]:
                ns = add(l, s, k)
                if ns not in dp[i][j]:
                    dp[i][j][ns] = 0
                dp[i][j][ns] = (dp[i][j][ns] + dp[i-1][j-k][l] * pow(states[s], k, mod) * c(j, k)) % mod

dp1 = [{} for i in range(m+1)]

dp1[0][0] = 1

for i in fixed_states:
    j = i[0] - i[1]
    dp1[1][j] = fixed_states[i]

for i in range(2, m+1):
    for j in dp1[1]:
        for k in dp1[i-1]:
            if j + k not in dp1[i]:
                dp1[i][j+k] = 0
            dp1[i][j+k] = (dp1[i][j+k] + dp1[1][j] * dp1[i-1][k]) % mod

ans = 0
for i in range(m+1):
    j = m-i
    for k in dp1[i]:
        for l in dp[-1][j]:
            if k + l[0] > 0:
                ans = (ans + dp1[i][k] * dp[-1][j][l] * c(m, i)) % mod

print(ans)