intersections = set()
from fractions import Fraction
import itertools

n = 5000
lines = []
mod = 50515093
s = 290797

for i in range(n):
    line = []
    for j in range(4):
        s = pow(s, 2, mod)
        line.append(s%500)
    lines.append(line)

def gradient(line : list) -> Fraction:
    return Fraction(line[3]-line[1], line[2]-line[0])

def constant(line : list, g : Fraction) -> Fraction:
    return line[1] - g * line[0]

def intersection(line1 : list, line2 : list) -> tuple:
    if line1[0] != line1[2] and line2[0] != line2[2]:
        g1 = gradient(line1)
        g2 = gradient(line2)
        c1 = constant(line1, g1)
        c2 = constant(line2, g2)

        if g1 == g2:
            return -1, 1

        return 1/(g2-g1) * (c1 - c2), 1/(g2-g1) * (g2*c1 - g1*c2)
    elif line1[0] == line1[2]:
        if line2[0] == line2[2]:
            return -1, 1
        else:
            x = line1[0]
            g2 = gradient(line2)
            c2 = constant(line2, g2)
            return x, g2*x+c2
    else:
        x = line2[0]
        g1 = gradient(line1)
        c1 = constant(line1, g1)
        return x, g1*x+c1

def interior(point : tuple, line : list) -> bool:
    x = min(line[0], line[2])
    y = max(line[0], line[2])
    p = min(line[1], line[3])
    q = max(line[1], line[3])
    return not ((point[0] <= x or point[0] >= y) and (point[1] <= p or point[1] >= q))


for i, j in itertools.combinations(lines, 2):
    point = intersection(i, j)
    if interior(point, i) and interior(point, j):
        intersections.add(point)

print(len(intersections))

