from fractions import Fraction
x: Fraction
x = Fraction(2, 1)
f = lambda x: 2+1/x

ans = 0
for i in range(1000):
    x = f(x)
    y = x-1
    if len(str(y.numerator)) > len(str(y.denominator)):
        ans += 1
print(ans)
