d = {0 : set([1,3,4,5,6,7]),
     1 : set([5,7]),
     2 : set([1,2,3,5,6]),
     3 : set([1,2,3,5,7]),
     4 : set([2,4,5,7]),
     5 : set([1,2,3,4,7]),
     6 : set([1,2,3,4,6,7]),
     7 : set([1,4,5,7]),
     8 : set([1,2,3,4,5,6,7]),
     9 : set([1,2,3,4,5,7])}

from prime import memoize

@memoize
def transition_digit(a, b):
    return len(d[b] - d[a]) + len(d[a] - d[b])

def transition(a, b):
    x = len(a)
    y = len(b)
    ans = 0
    for i in range(x-y):
        ans += len(d[int(a[i])])
    for i in range(y):
        ans += transition_digit(int(a[i+x-y]), int(b[i]))
    return ans

def digital_root1(x):
    ans = 0
    while x >= 10:
        y = str(x)
        for i in y:
            ans += len(d[int(i)]) * 2
        x = sum(int(i) for i in y)
    y = str(x)
    for i in y:
        ans += len(d[int(i)]) * 2
    return ans

def digital_root2(x):
    ans = 0
    y = str(x)
    for i in y:
        ans += len(d[int(i)])
    prev = y
    while x >= 10:
        x = sum(int(i) for i in y)
        y = str(x)
        ans += transition(prev, y)
        prev = y
    for i in prev:
        ans += len(d[int(i)])
    return ans

from prime import primes

p = primes(2*10**7)
l = 10**7

# p = [10]
# l = 0
ans = 0
for i in p:
    if i > l:
        ans += digital_root1(i) - digital_root2(i)
print(ans)