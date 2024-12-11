from fractions import Fraction

def solveMatrix(M, x):
    for i in range(len(M)):
        if M[i][i] == 0:
            print("Fail")
        for j in range(len(M)):
            if j == i or M[j][i] == 0:
                continue
            c = M[j][i] / M[i][i]
            for k in range(len(M)):
                M[j][k] -= M[i][k] * c
            x[j] -= x[i] * c
    for i in range(len(M)):
        x[i] /= M[i][i]
    # print(M, x)
    return x

M = [[0 for i in range(100)] for j in range(100)]
v = [1 for i in range(100)]
v[0] = Fraction(0, 1)

for i in range(1,100):
    M[i][(i+1)%100] = -2 * Fraction(1, 6) * Fraction(4, 6)
    M[i][(i-1)%100] = -2 * Fraction(1, 6) * Fraction(4, 6)
    M[i][(i+2)%100] = -Fraction(1, 36)
    M[i][(i-2)%100] = -Fraction(1, 36)
    M[i][i] = -Fraction(18, 36)

for i in range(100):
    M[i][i] += 1

s = solveMatrix(M, v)
print("{:.6f}".format(s[50].numerator/s[50].denominator))
