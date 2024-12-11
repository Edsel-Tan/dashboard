import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def normsq(self):
        return self.x**2 + self.y**2
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, d):
        return Vector(self.x * d, self.y * d)
    
    def __truediv__(self, d):
        return Vector(self.x/d, self.y/d)
    
    def __str__(self):
        return f"{self.x}i + {self.y}j"
    
    def __repr__(self):
        return self.__str__()
    
g = Vector(5000,0)
m = Vector(-5000,0)

d = 15000
rt2 = math.sqrt(2)
f = lambda p: ((p-g).normsq() + (p-m).normsq() - d**2) / ((p-m).norm() * (p-g).norm())
ans = 0

x = 0
p = Vector(x,0)
while (p-g).norm() + (p-m).norm() <= d:
    p.x += 1

while f(p) <= rt2:
    ans += 2
    p.x += 1


y = 0
p = Vector(0,y)
while (p-g).norm() + (p-m).norm() <= d:
    p.y += 1

while f(p) <= rt2:
    ans += 2
    p.y += 1

x = 1
y = 1
p = Vector(x, y)
b = True

while b:
    
    b = False
    while (p-g).norm() + (p-m).norm() <= d:
        p.y += 1

    while f(p) <= rt2:
        b = True
        ans += 4
        p.y += 1

    p.x += 1
    p.y = 1

print(ans)


