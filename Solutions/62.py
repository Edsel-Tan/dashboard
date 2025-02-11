s = {}
ans = {}
n = 10000
for i in range(1, n+1):
    key = ''.join(sorted(str(i**3)))
    if key not in s:
        s[key] = 0
        ans[key] = n
    s[key] += 1
    ans[key] = min(ans[key], i)

a = n
for i in s:
    if s[i] == 5:
        a = min(a, ans[i])
print(a**3)