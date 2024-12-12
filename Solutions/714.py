from prime import pollard_rho
import itertools
import math

n = 50000
m = 9
ans = [math.inf for i in range(n+1)]

remaining = [8910, 9890, 17820, 18890, 19780, 20410, 22090, 22670, 24130, 24590, 26730, 27710, 28330, 29530, 29670, 29990, 30970, 31330, 31690, 31970, 32290, 32330, 32570, 33830, 33890, 34130, 34390, 35110, 35470, 35640, 36010, 36170, 36230, 37090, 37210, 37330, 37490, 37780, 37990, 38510, 39010, 39430, 39530, 39560, 39890, 40820, 41210, 41330, 41570, 42710, 43030, 43270, 44180, 44550, 44710, 45190, 45340, 45470, 45490, 46030, 46430, 46570, 47090, 47170, 47230, 47290, 47690, 48130, 48260, 48670, 48710, 48830, 49180, 49450, 49790, 49990]
def factors_sub(x):
    output = []
    for i in remaining:
        if x % i == 0:
            output.append(i)
    return output

def f(a,b,c):
    if c == 1:
        yield a
        return
    for i in f(a,b,c-1):
        yield i * 10 + a
        yield i * 10 + b
    return

for a in range(1,10):
    for i in f(a,0,16):
        if i == 0:
            continue
        for j in factors_sub(i):
            ans[j] = min(ans[j], i)
    for i in f(a,0,17):
        if i == 0:
            continue
        for j in factors_sub(i):
            ans[j] = min(ans[j], i)
    for i in f(a,0,18):
        if i == 0:
            continue
        for j in factors_sub(i):
            ans[j] = min(ans[j], i)
    for i in f(a,0,19):
        if i == 0:
            continue
        for j in factors_sub(i):
            ans[j] = min(ans[j], i)
    for i in f(a,0,20):
        if i == 0:
            continue
        for j in factors_sub(i):
            ans[j] = min(ans[j], i)

r = 32570
for a in range(1,10):
    for i in f(a,0,21):
        if i == 0:
            continue
        if i % r == 0:
            ans[r] = min(ans[r], i)
    for i in f(a,0,22):
        if i == 0:
            continue
        if i % r == 0:
            ans[r] = min(ans[r], i)


a = 0
for i in remaining:
    a += ans[i]
print("{:.12E}".format(float(a+33829876565880586)))