limit = 28123
divsum = [1 for i in range(limit+1)]

for i in range(2, limit+1):
    for j in range(2*i, limit+1, i):
        divsum[j] += i

abundant = []
for i in range(1, limit+1):
    if divsum[i] > i:
        abundant.append(i)

s = set()
for i in abundant:
    for j in abundant:
        s.add(i+j)
ans = 0
for i in range(1, limit+1):
    if i not in s:
        ans += i
print(ans)