import math
import itertools
tolerance = 0.00001

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

class Line:
    
    def __init__(self, point1 : Point, point2 : Point):
        self.x = (point2.x - point1.x, point1.x)
        self.y = (point2.y - point1.y, point1.y)


def intersects(line1 : Line, line2 : Line):
    a1 = line1.x[0]
    b1 = line1.x[1]
    a2 = line2.x[0]
    b2 = line2.x[1]
    c1 = line1.y[0]
    d1 = line1.y[1]
    c2 = line2.y[0]
    d2 = line2.y[1]

    x = b2 - b1
    y = d2 - d1

    det = 1 / (a2 * c1 - a1 * c2)
    t = det * (-c2 * x + a2 * y)
    t_ = det * (-c1 * x + a1 * y)

    # print(t, t_, t >= 0-tolerance and t <= 1+tolerance and t_ >= 0-tolerance and t_ <= 1+tolerance)
    if t >= 0-tolerance and t <= 1+tolerance and t_ >= 0-tolerance and t_ <= 1+tolerance:
        return True
    return False
    
linecollection = []
n = 36
rt3 = math.sqrt(3)

b1 = []
b2 = []
b3 = []

for i in range(2*n+1):
    b1.append(Point(i*2, 0))
    b2.append(Point(i, i*rt3))
    b3.append(Point(n*2 + i, n*2*rt3 - i*rt3))

l1 = []
l2 = []
l3 = []
for i in range(n):
    l1.append(Line(b1[2*i+2], b2[2*i+2]))
    l2.append(Line(b1[2*i], b3[2*i]))
    l3.append(Line(b2[2*i], b3[2*n-2*i]))
linecollection.append(l1)
linecollection.append(l2)
linecollection.append(l3)

l1 = []
l2 = []
l3 = []
for i in range(n):
    l1.append(Line(b1[i+1], b2[2*i+2]))
    l2.append(Line(b2[i+1], b1[2*i+2]))
    l3.append(Line(b3[i+1], b2[2*n-2-2*i]))


for i in range(n-1):
    l1.append(Line(b1[n+i+1], b3[2*i+2]))
    l2.append(Line(b2[n+i+1], b3[2*n-2-2*i]))
    l3.append(Line(b3[n+i+1], b1[2*i+2]))

linecollection.append(l1)
linecollection.append(l2)
linecollection.append(l3)


ans = 0
for lc1, lc2, lc3 in itertools.combinations(linecollection, 3):
    for l1 in lc1:
        for l2 in lc2:
            for l3 in lc3:
                if intersects(l1, l2) and intersects(l2, l3) and intersects(l1, l3):
                    ans += 1

ans -= 3
ans -= (((n+1) * (n+2))//2 - 3) * 20
ans -= n**2
print(ans)
    



