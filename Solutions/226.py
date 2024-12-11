from fractions import Fraction # type: ignore
import math

precision = 2**64

def f(x):
    if x > Fraction(1,2):
        x = 1 - x

    if x == 0:
        return 0

    return x + f(2*x)/2

def distance(a, b, x, y):
    return math.sqrt((a-x)**2 + (b-y)**2)

l = Fraction(0,1)
r = Fraction(1,4)

while l.denominator < precision:
    m = (l+r)/2
    if distance(m, f(m), 0.25, 0.5) > 1/4:
        l = m
    else:
        r = m

m = (l+r)/2


def integrate(a, b, x, y):
    return (x-a) * b + 0.5 * (x-a) * (y-b)

#area outside circle
h = 1/4
b = 0.5 * distance(m, f(m), 0.5, 0.5)
theta = 2 * math.asin(b/h)
ac = integrate(m, f(m), 0.5, 0.5) - (1/2 * theta * (h ** 2) - 1/2 * (h ** 2) * math.sin(theta))
#area under graph
ag = 0
denominator = 1
while denominator < m.denominator:
    l = Fraction(0,1)
    r = Fraction(1,1)
    while r-l > Fraction(1, 2*denominator):
        n = (l+r)/2
        if n > m:
            r = n
        else:
            l = n
    # l = Fraction(l, 2*denominator)
    # r = Fraction(r, 2*denominator)
    if r.denominator < l.denominator:
        ag += ((r-m) * 2)**2 * (1/8)
    else:
        ag += (Fraction(1, 8*denominator**2)) - ((m-l) * 2)**2 * (1/8)
    
    ag += Fraction(1, 4*denominator) * (Fraction(1,2) - r)
    denominator = denominator*2

ag += (Fraction(1,2) - m) * (Fraction(1,2 * m.denominator))
print("{:.8f}".format(ag-ac))


