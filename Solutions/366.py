n = 10**18
fib = [2,3]
while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])

def find(x):
    l, r = 0, len(fib)-1
    while (r-l):
        m = (l+r+1)//2
        if fib[m] <= x:
            l = m
        else:
            r = m-1
    return l

dp = [0]

def M(x):
    if x <= 3:
        return 0
    idx = find(x)
    y = x - fib[idx]
    if y * 2 < fib[idx]:
        return dp[idx] + (y * (y+1))//2
    z = (fib[idx]-1)//2
    return dp[idx] + (z * (z+1))//2 + M(y) - M(z)

for i in fib[1:]:
    dp.append(M(i-1))

print(M(10**18)%(10**8))