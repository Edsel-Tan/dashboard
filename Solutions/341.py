dp = [0,1,3]
def idx(x):
    l,r = 0, len(dp)-1
    while (r-l):
        m = (l+r)//2
        if dp[m] >= x:
            r = m
        else:
            l = m+1
    return l

n = 2*10**7
for i in range(3, n+1):
    dp.append(dp[-1] + idx(i))

dp2 = [1]
for i in range(1, n):
    dp2.append(dp2[-1] + (i+1) * (dp[i+1] - dp[i]))

def f(x):
    l, r = 0, len(dp)-1
    while (r-l):
        m = (l+r)//2
        if dp2[m] >= x:
            r = m
        else:
            l = m+1
    return dp[l] + (x - dp2[l-1] - 1) // (l+1) + 1

ans = 1
for i in range(2, 10**6):
    ans += f(i**3)
print(ans)