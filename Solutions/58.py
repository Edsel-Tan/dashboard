f = lambda x: 4*x*x - 10*x + 7
g = lambda x: 4*x*x - 8*x + 5
h = lambda x: 4*x*x - 6*x + 3

from prime import miller_rabin

cnt = 0
for i in range(2, 10**6):
    if miller_rabin(f(i)):
        cnt += 1
    if miller_rabin(g(i)):
        cnt += 1
    if miller_rabin(h(i)):
        cnt += 1
    if cnt <= (4*(i-1) + 1) // 10:
        break
print(2*i-1)