from fractions import Fraction # type: ignore

s = set()
for i in range(1864, 1910):
    for j in range(i):
        s.add(Fraction(j, i))
        
print(len(s))