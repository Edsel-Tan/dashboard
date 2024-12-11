from fractions import Fraction # type: ignore

s = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
# s = "DdDddUUdDD"

def d(a, b):
    return (3 * a / 2, (3 * b + 1) / 2)

def U(a, b):
    return (3 * a / 4, (3 * b - 2) / 4)

def D(a, b):
    return (3 * a, 3 * b)

a = Fraction(1, 1)
b = Fraction(0, 1)

for i in s[::-1]:
    if i == 'd':
        a, b = d(a, b)
    elif i == 'U':
        a, b = U(a, b)
    elif i == 'D':
        a, b = D(a, b)

x = (-b.numerator * pow(a.numerator, -1, a.denominator))%a.denominator
m = (10**15-b)//a + 1
c = (((m-x) // a.denominator) + 1) * a.denominator + x
print(a*c+b)