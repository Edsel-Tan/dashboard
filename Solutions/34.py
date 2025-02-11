f = [1]
for i in range(1,10):
    f.append(f[-1] * i)

def s(x):
    output = 0
    while x > 0:
        output += f[x%10]
        x = x//10
    return output

ans = 0
for i in range(10,10**6):
    if s(i) == i:
        ans += i

print(ans)