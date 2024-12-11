from prime import memoize

cache = {1:1}

n = 10**6
ans = 0
for j in range(1, n+1):
    c = 0
    i = j
    while i not in cache:
        if i % 2 == 0:
            i = i//2
        else:
            i = 3*i+1
        c += 1
    cache[j] = cache[i] + c
    ans = max(ans, cache[i] + c)
for i in range(1, n+1):
    if cache[i] == ans:
        print(i)
        break