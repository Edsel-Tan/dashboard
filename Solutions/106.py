import itertools

def C(n, m):
    if m > n//2:
        m = n - m
    output = 1
    for i in range(m):
        output *= n-i
    for i in range(m):
        output //= i+1
    return output

n = 12

def f(lis):
    for i in range(len(lis)):
        if lis[i] <= 2*i:
            return 0
    return 1

new = 0
for i in range(n//2):
    ans = 0
    for j in itertools.combinations(range(2*i+2), i+1):
        ans += f(j)
    new += (C(2*i+2, i+1)//2 - ans) * C(n, 2*i+2)
print(new)
