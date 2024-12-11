
def U(a, b, n):
    usums = set()
    sums = set()
    sums.add(a+b)
    usums.add(a+b)
    numbers = [a, b]
    while len(numbers) < n:
        u = min(usums)
        usums.remove(u)
        for i in numbers:
            if i + u not in sums:
                usums.add(i + u)
                sums.add(i + u)
            else:
                try:
                    usums.remove(i+u)
                    # print(i, u, sums)
                except:
                    pass
        numbers.append(u)
    return numbers

def efficientU(b, n):
    evens = [2, 2*b+2]
    usums = set()
    sums = set()
    numbers = [2,b]
    sums.add(2+b)
    usums.add(2+b)
    sums.add(3*b+2)
    usums.add(3*b+2)
    while len(numbers) < n:
        u = min(usums)
        usums.remove(u)
        for i in evens:
            if i + u not in sums:
                usums.add(i+u)
                sums.add(i+u)
            else:
                try:
                    usums.remove(i+u)
                except:
                    pass
        numbers.append(u)
    return numbers



kk = 10**11 - 2
ans = 0
for i in range(2, 11):
    s = efficientU(2*i+1, 10000000)
    ds = [s[i] - s[i-1] for i in range(1, len(s))]
    t = max(ds)
    period = []
    for i in range(len(ds)):
        if ds[i] == t:
            period.append(i)
    period = period[1] - period[0]
    start = ds.index(t)
    diff = s[start+period] - s[start]

    k = kk - start
    q = k // period
    r = k % period

    a = s[start+r]
    a += q * diff
    ans += a
    
print(ans)
    


    
