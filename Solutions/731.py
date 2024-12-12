z = 15
k = 16
n = 10**k + z-1
mod = 10**z

x = 3
tx = 2
ans = 0
while x < n:
    r = pow(10, (n-x)%tx, x)
    ans = (ans + (-r)*pow(x, -1, mod)) % mod
    x = x*3
    tx = tx*3

print(ans)
