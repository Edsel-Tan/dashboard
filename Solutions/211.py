
n = 64000000
sigma2 = [0 for i in range(n+1)]

for i in range(1, n+1):
    c = i ** 2
    for j in range(i, n+1, i):
        sigma2[j] += c
    

square = set()
for i in range(1,2*n):
    square.add(i**2)


ans = 0
for i in range(1, n+1):
    if sigma2[i] in square:
        ans += i

print(ans)