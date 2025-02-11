n = 10**16
mod1 = 10**11
mod2 = 10**9 + 7
f = lambda x, y: (x*x+2)%y

ans = 0

cyc_sum = 0
cyc_len = 0
x = 0
y = 0

while True:
    x = f(x, mod2)
    y = f(f(y, mod2), mod2)
    cyc_len += 1
    if x == y:
        break
    ans = (ans + x) % mod2

for i in range(cyc_len):
    cyc_sum = (cyc_sum + x) % mod2
    x = f(x, mod2)

ans = (ans + ((n - cyc_len + 1) // (cyc_len)) * cyc_sum) % mod2

for i in range((n+1)%cyc_len):
    ans = (ans + y) % mod2
    y = f(y, mod2)

def g(x):
    z = x % 10
    d = []
    while True:
        d.append(x % 10)
        if x % 10 < z:
            break
        z = x % 10
        x = x // 10
    original = 0
    for i in reversed(d):
        original *= 10
        original += i
    y = d[-1]
    for i in d:
        if i > y:
            break
    d.remove(i)
    next = i
    for i in sorted(d):
        next *= 10
        next += i
    return next - original


cyc_sum = 0
cyc_len = 0
x = 0
y = 0

while True:
    x = f(x, mod1)
    y = f(f(y, mod1), mod1)
    cyc_len += 1
    if x == y:
        break
    ans = (ans + g(x)) % mod2

for i in range(cyc_len):
    cyc_sum = (cyc_sum + g(x)) % mod2
    x = f(x, mod1)

ans = (ans + ((n - cyc_len + 1) // (cyc_len)) * cyc_sum) % mod2

for i in range((n+1)%cyc_len):
    ans = (ans + g(y)) % mod2
    y = f(y, mod2)

ans -= 2 + 6 + g(2) + g(6)
print(ans % mod2)