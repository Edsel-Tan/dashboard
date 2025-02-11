f = [
    lambda x: (x*(x+1))//2,
    lambda x: x*x,
    lambda x: (x*(3*x-1))//2,
    lambda x: x*(2*x-1),
    lambda x: (x*(5*x-3))//2,
    lambda x: x*(3*x-2)
]

t = [{} for i in f]
for i in range(len(f)):
    g = f[i]
    for j in range(1000):
        x = g(j)
        if x <= 1000:
            continue
        if x >= 10000:
            break
        if x//100 not in t[i]:
            t[i][x//100] = []
        t[i][x//100].append(x%100)


import itertools
ans = []
for order in itertools.permutations(range(1, len(f)), len(f)-1):
    for start in t[0]:
        for next in t[0][start]:
            ans = [start*100 + next]
            
            def f(i):
                global order, ans, start, next
                if i >= len(order):
                    if start == next:
                        print(sum(ans))
                        exit()
                    return
                if next not in t[order[i]]:
                    return
                for j in t[order[i]][next]:
                    ans.append(next*100 + j)
                    next = j
                    f(i+1)
                    ans.pop()

            f(0)
