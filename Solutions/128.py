from prime import miller_rabin, memoize

ranges = []
m = 200000
for i in range(m):
    ranges.append(3*i*(i+1)+2)

def t(*args):
    print(*args)
    return miller_rabin(*args)

mr = memoize(miller_rabin)
def f(n, i):
    if i < 0:
        return ranges[n+1] + i
    return ranges[n] + i

def PD(n, i):
    m = f(n,i)
    count = 0
    if i == 0 or i == 6*n+5:
        count += mr(6*n+5)
    if i % (n+1) == 0:
        for j in range(i//(n+1) * (n+2) - 1, i//(n+1) * (n+2) + 2):
            count += mr(abs(m - f(n+1, j)))
        count += mr(abs(m - f(n-1, i//(n+1) * n)))
    else:
        for j in range(i + i//(n+1), i + i//(n+1) + 2):
            count += mr(abs(m - f(n+1, j)))
        for j in range(i - i//(n+1) - 1, i - i//(n+1) + 1):
            count += mr(abs(m - f(n-1, j % (6*n))))
    return count
        

ans = []
for i in range(1, m-2):
    for j in range(0, 6*i+6, i+1):
        if PD(i, j) == 3:
            ans.append(f(i, j))
    if PD(i, 6*i+5) == 3:
        ans.append(f(i, 6*i+5))
print(ans[1997])
