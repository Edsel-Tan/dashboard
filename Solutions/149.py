import math

def findMaxSubsequence(arr : list) -> int:
    # return sum(arr)
    prefixSum = [0]
    for i in arr:
        prefixSum.append(prefixSum[-1] + i)
    minSum = math.inf
    output = 0
    for i in prefixSum:
        minSum = min(i, minSum)
        output = max(output, i - minSum)
    return output

s = []
for i in range(55):
    # s.append(0)
    s.append((100003 - 200003 * (i+1) + 300007 * (i+1) ** 3) % 1000000 - 500000)
for i in range(4000000-55):
    # s.append(0)
    s.append((s[-24] + s[-55] + 1000000) % 1000000 - 500000)

# print(s[9], s[99])
ans = 0
# rows
for i in range(2000):
    row = []
    for j in range(2000):
        row.append(s[2000*i + j])
    ans = max(ans, findMaxSubsequence(row))

for i in range(2000):
    col = []
    for j in range(2000):
        col.append(s[i+2000*j])
    ans = max(ans, findMaxSubsequence(col))

for i in range(3999):
    diagonal = []
    for x in range(max(0, i-1999), min(i+1, 2000)):
        y = i - x
        diagonal.append(s[2000*y + x])
    ans = max(ans, findMaxSubsequence(diagonal))

    diagonal = []
    j = i - 1999
    for x in range(max(0, j), min(2000, 2000+j)):
        y = x - j
        diagonal.append(s[2000*y+x])
    ans = max(ans, findMaxSubsequence(col))

print(ans)