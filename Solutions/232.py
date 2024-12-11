n = 100
from fractions import Fraction # type: ignore

dp = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(n+1):
    dp[n][i] = 0
    dp[i][n] = 1

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        t = 0
        mp = 0
        while 2 ** (t-1) <= n - j:
            t += 1
            cp = 0
            p = Fraction(1, 2**t)
            cp += p * Fraction(1,2) * dp[i+1][min(j+2**(t-1), n)]
            cp += p * Fraction(1,2) * dp[i][min(j+2**(t-1), n)]
            cp += (1-p) * Fraction(1,2) * dp[i+1][j]
            mp = max(mp, cp/(1 - Fraction(1,2) * (1-p)))
        dp[i][j] = mp

# print(dp[1][0].numerator/dp[1][0].denominator)
print("{:.8f}".format(0.5 * (dp[0][0].numerator/dp[0][0].denominator) + 0.5 * (dp[1][0].numerator/dp[1][0].denominator)))