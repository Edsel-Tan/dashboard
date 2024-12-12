import itertools

k = 25
f = lambda x: (25+x)/100

def prob(states):
    pH = 0.5
    pT = 0.5
    for i in range(k):
        pH *= abs(states[i] - f(i))
        pT *= abs(1 - states[i] - f(i))
    return pH, pT

probs = []
for state in itertools.product(range(2), repeat=k):
    pH, pT = prob(state)
    probs.append((max(pH, pT)/min(pH, pT), max(pH, pT), pH+pT))
probs = sorted(probs)
n = len(probs)

ans = 0
cum = 0
p = 0
for i in range(n):
    x, y, z = probs[i]
    p += z * z + 2 * z * cum
    ans += (z * z + 2 * z * cum) * y / z
    cum += z
print("{:.10f}".format(ans))