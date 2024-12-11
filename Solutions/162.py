n = 16
import itertools

c = list(range(n))

ans = 0
ans1 = 0
for x in range(n):
    c = list(range(x+1))
    for i,j,k in itertools.combinations(c, 3):
        # print(i, j, k)
        if i == 0:
            ans += 14**(j-i-1) * 15**(k-j-1) * 16 ** (x-k) * 4
        else:
            ans += 13 ** i * 14**(j-i-1) * 15**(k-j-1) * 16 ** (x-k) * 6
            # ans1 += 14 * 15 ** (i-1) * 14**(j-i-1) * 15**(k-j-1) * 16 ** (x-k) * 4
            # ans += (15 * 16 ** (i-1) if i != 0 else 1) * 14**(j-i-1) * 15**(k-j-1) * 16 ** (x-k) * (4 if i == 0 else 6)

count = 0
for i in range(16**4-1):
    s = hex(i)[2:]
    count += s.count('a') > 0 and s.count('0') > 0 and s.count('1') > 0

print(hex(ans)[2:].upper())