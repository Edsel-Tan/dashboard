from prime import primes
from fractions import Fraction # type: ignore

# states = dict(zip([i for i in range(0, 501)], [{} for i in range(1, 501)]))
states = [{} for i in range(501)]
p = set(primes(501))

for i in range(1,  501):
    if i in p:
        states[i][1] = {}
        states[i][1]["P"] = Fraction(2, 3)
        states[i][1]["N"] = Fraction(1, 3)

    else:
        states[i][1] = {}
        states[i][1]["P"] = Fraction(1, 3)
        states[i][1]["N"] = Fraction(2, 3)


for k in range(2, 16):
    states[1][k] = {}
    states[500][k] = {}
    for j in states[2][k-1].keys():
        states[1][k]["P"+j] = Fraction(1, 3) * states[2][k-1][j]
        states[1][k]["N"+j] = Fraction(2, 3) * states[2][k-1][j]
    for j in states[499][k-1].keys():
        states[500][k]["P"+j] = Fraction(1, 3) * states[499][k-1][j]
        states[500][k]["N"+j] = Fraction(2, 3) * states[499][k-1][j]
    for i in range(2, 500):
        states[i][k] = {}
        if i in p:
            P = Fraction(2, 6)
            N = Fraction(1, 6)
        else:
            P = Fraction(1, 6)
            N = Fraction(2, 6)
        for j in states[i-1][k-1].keys():
            states[i][k]["P"+j] = P * states[i-1][k-1][j]
            states[i][k]["N"+j] = N * states[i-1][k-1][j]
        for j in states[i+1][k-1].keys():
            states[i][k]["P"+j] += P * states[i+1][k-1][j]
            states[i][k]["N"+j] += N * states[i+1][k-1][j]


# print(states[2][4])
key = "PPPPNNPPPNPPNPN"

ans = 0
for i in range(1, 501):
    ans += states[i][len(key)][key]
print(ans/500)