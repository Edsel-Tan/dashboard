from prime import primes

p = primes(10000)
s = []
for i in p:
    if i > 1000:
        s.append(i)
t = set(s)

def f(x, y):
    return sorted(str(x)) == sorted(str(y))

for i in range(len(s)):
    if s[i] == 1487:
        continue
    for j in range(i+1, len(s)):
        if f(s[i], s[j]) and (s[i] + s[j])//2 in t and f(s[i], (s[i] + s[j])//2):
            print(str(s[i]) + str((s[i] + s[j])//2) + str(s[j]))
            break
