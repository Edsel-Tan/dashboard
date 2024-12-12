n = 10**12

m = 904961
x = n//8

ans = n//4 * (m+1)
while x:
    ans += x * (m+1)
    x = x//2

print(ans)