from fractions import Fraction # type: ignore

dp = [[set() for i in range(9)] for j in range(9)]

for i in range(9):
    dp[0][i].add(Fraction(i+1, 1))

for i in range(1, 9):
    for j in range(9-i):
        for k in range(1, i+1):
            for x in dp[k-1][j]:
                for y in dp[i-k][j+k]:
                    dp[i][j].add(x+y)
                    dp[i][j].add(x-y)
                    if y != 0:
                        dp[i][j].add(x/y)
                    dp[i][j].add(x*y)
        dp[i][j].add(Fraction(int("".join([str(i) for i in range(j+1, j+i+2)])), 1))

ans = 0
for i in dp[8][0]:
    if i.denominator == 1 and i > 0:
        ans += i.numerator
        
print(ans)
    

