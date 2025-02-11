s = set()
l = 10**7
f = lambda x: (x*(3*x-1))//2

for i in range(1,l):
    x = f(i)
    if x > l:
        break
    s.add(f(i))

ans = l
for i in s:
    for j in s:
        if i + j in s and i - j in s:
            ans = min(ans, i-j)
print(ans)