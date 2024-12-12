state = []
curr = 0
x = 0
m = 0
l = 0

ans = 0
n = 16

def f(k, z):
    global curr
    total = 0
    if x > m:
        return 0
    if len(state) == x:
        if sorted(str(curr+1), reverse=True) == state:
            return curr+1
        if sorted(str(curr-1), reverse=True) == state:
            return curr-1
        else:
            return 0
    if z < 0:
        return 0
    c = len(state)
    if curr + (x-c) * z ** k < l:
        return 0
    total += f(k, z-1)
    for i in range(x-c):
        state.append(str(z))
        curr += z ** k
        total += f(k, z-1)
    while len(state) > c:
        state.pop()
        curr -= z ** k
    return total

for i in range(2, n+1):
    x = i
    m = 10**x
    l = 10**(x-1)
    for j in range(20):
        ans += f(j, 9)
print(ans)