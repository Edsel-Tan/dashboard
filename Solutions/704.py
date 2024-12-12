ans = 0
n = 10**16
l,r = 1,2
c = 0

while l < n+1:
    ans += (min(r,n+1)-l)*c
    c += 1
    r *= 2
    l *= 2

x = 1
while x <= n:
    ans -= (n+1)//(x+1) - 1
    x *= 2
    x += 1

print(ans)