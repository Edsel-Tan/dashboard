from prime import primes
import math

n = 10**11
m = math.isqrt(n)
l = 9*7*13*19
t = 5

p = primes(n//l+1)

p1 = [3]
for i in p:
    if i % 3 == 1:
        p1.append(i)

s = set()
for i in range(1, m+1):
    s.add(i)
    s.add(n//i)
s = sorted(s)

f = lambda x : x - 1 if x < m else len(s) - (n // x) 

dp = [(i*(i+1))//2 for i in s]

for i in range(len(p1)):
    for j in range(len(s)-1, -1, -1):
        if s[j] < p1[i]:
            break
        dp[j] -= dp[f(s[j]//p1[i])] * p1[i]



ans = 0
stack = [[1,t,1], [3,t,1]]

c = 9
while c < n//l:
    stack.append([c,t-1,1])
    c *= 3

while len(stack) > 0:
    top = stack[-1]
    del stack[-1]

    if top[1] == 0:
        ans += dp[f(n//top[0])] * top[0]
        continue

    if top[2] >= len(p1):
        continue

    if top[0] * p1[top[2]] > n:
        continue

    top[2] += 1
    stack.append(top.copy())
    
    top[1] -= 1
    top[0] *= p1[top[2]-1]
    while top[0] <= n:
        stack.append(top.copy())
        top[0] *= p1[top[2]-1]

print(ans)
    

