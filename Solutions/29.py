a = 100
b = 100

l = [i for i in range(a+1)]
for i in range(2, a+1):
    j = i
    while j < a+1:
        l[j] = min(i, l[j])
        j *= i

count = {}
for i in range(2, a+1):
    if l[i] not in count:
        count[l[i]] = 0
    count[l[i]] += 1

def f(x):
    s = set()
    for i in range(1, x+1):
        for j in range(2, b+1):
            s.add(i*j)
    return len(s)

ans = 0
for i in range(2, a+1):
    if l[i] == i:
        ans += f(l.count(i))
print(ans)