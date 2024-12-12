from prime import primes
import math

n = 10**12
m = math.isqrt(n)
p = primes(m+1)
k = 20

s = set()
for i in range(1, m+1):
    s.add(n//i)
    s.add(i)
s = sorted(s)

f = lambda x : x - 1 if x < m else len(s) - (n // x) 

dp = [i for i in s]

for i in range(len(p)):
    for j in range(len(s)-1, -1, -1):
        if s[j] < p[i] * p[i]:
            break
        # print(i, j)
        dp[j] -= dp[f(s[j]//p[i])] - (i+1)

for i in range(len(dp)):
    dp[i] -= 1



ans = 0
stack = [[n, 0, k]]


while len(stack) != 0:
    st = stack[-1]
    del stack[-1]

    if st[0] == 0 or st[2] == 0:
        ans += 0
        continue

    if st[0] == 1 or st[2] == 1:
        ans += 1
        # print("1", st[0])
        continue

    if st[1] == len(p):
        ans += max(dp[f(st[0])] - st[1] + 1, 1)
        # print("3", max(dp[f(st[0])] - st[1] + 1, 1))
        continue

    if p[st[1]] > st[0]:
        ans += 1
        # print("4", 1)
        continue
    
    if p[st[1]] ** 2 > st[0]:
        ans += max(dp[f(st[0])] - st[1] + 1, 1)
        # print("5", max(dp[f(st[0])] - st[1] + 1, 1), dp[f(st[0])])
        continue




    ss = st.copy()
    ss[1] += 1
    stack.append(ss)

    t = p[st[1]]
    i = 1
    while t <= st[0]:
        ss = st.copy()
        ss[2] = ss[2] // (2*((i+1)//2))
        ss[1] += 1
        ss[0] = ss[0] // t
        stack.append(ss)

        t = t * p[st[1]]
        i += 1

ans -= 1
print(ans - dp[f(n)] - dp[f(m)])