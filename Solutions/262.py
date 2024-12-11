import math
dx = 0.0000001
dy = dx

z = lambda x,y : ( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) )
h = lambda x,y : ( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * math.exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )
dhx = lambda x,y : (h(x+dx,y)-h(x,y))/dx
dhy = lambda x,y : (h(x,y+dy)-h(x,y))/dy

dxh = lambda x,y : -(0.000001*(2*x)-0.0015*(x)) * ( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * math.exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7)) + ( -0.005*(2*x+y)+12.5*(x) ) * math.exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7))
dyh = lambda x,y : dxh(y,x)

#Prelim

m = (0,0)

for i in range(1600000):
    x = i/1000

    if m[0] < h(x, 0):
        m = (h(x,0), x, 0)
    if m[0] < h(x, 1600):
        m = (h(x,1600), x, 1600)
    if m[0] < h(0, x):
        m = (h(0,x), 0, x)
    if m[0] < h(1600, x):
        m = (h(1600,x), 1600, x)

#Precise

for i in range(2000000):
    x = i/1000000/1000 + 878.540

    if m[0] < h(x, 0):
        m = (h(x,x), x, 0)



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"{self.x} {self.y}"
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.y - self.y * other.x
        elif isinstance(other, float):
            return Vector(other*self.x, other*self.y)
        
    def n(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def norm(self):
        d = math.sqrt(self.x**2 + self.y**2)
        return Vector(self.x/d, self.y/d)
    
    def dist(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)


dl = 0.001
def tangent(v, e):
    x = v.x
    y = v.y
    dx = dhx(x, y)
    dy = dhy(x, y)

    v1 = Vector(-dy, dx).norm()
    v2 = Vector(dy, -dx).norm()
    d1 = (v+v1*dl).dist(e)
    d2 = (v+v2*dl).dist(e)
    if d1 < d2:
        return v1
    else:
        return v2


end = Vector(200,200)
start = Vector(m[1], m[2])
curr = start
l = 0

while tangent(curr, end) * (end - curr) < 0:
    l += dl
    v = tangent(curr, end)
    curr = curr + v * dl
l += curr.dist(end)

start = Vector(m[1], m[2])
end = Vector(1400, 1400)
curr = start

while tangent(curr, end) * (end - curr) > 0:
    l += dl
    v = tangent(curr, end)
    curr = curr + v * dl
l += curr.dist(end)
print("{:.3f}".format(l))


