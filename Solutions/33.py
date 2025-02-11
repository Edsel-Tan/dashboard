from fractions import Fraction

ans = 1
for x in range(10, 99):
    for y in range(10, 99):
        if y%10 == 0:
            continue
        if Fraction(x, y) == Fraction(x//10, y%10) and (x%10) == (y//10) and x%11 > 0:
            ans *= Fraction(x,y)
print(ans.denominator)