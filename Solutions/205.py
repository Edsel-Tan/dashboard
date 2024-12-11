from fractions import Fraction # type: ignore
import itertools

peter = dict(zip(range(4,37), [0 for i in range(4, 37)]))
p = Fraction(1, 4**9)
for i in itertools.product([i+1 for i in range(4)], repeat = 9):
    peter[sum(i)] += p

collins = dict(zip(range(6,37), [0 for i in range(6, 37)]))
p = Fraction(1, 6**6)
for i in itertools.product([i+1 for i in range(6)], repeat = 6):
    collins[sum(i)] += p

ans = 0
base = 0
for i in range(7, 37):
    base += collins[i-1]
    ans += peter[i] * base
print("{:.7f}".format(ans.numerator/ans.denominator))