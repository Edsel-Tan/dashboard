from math import sqrt, sin, cos, acos, asin, pi

x = 100/sqrt(2)
y = 100/sqrt(2)

l = 0
r = pi/2
eps = 1e-15

while r-l > eps:
    m = (l+r)/2
    tx = 0
    t = 0
    dy = cos(m)
    dx = sin(m)
    tx += (y-50)/dy * dx
    t += ((y-50)/(10*dy))

    prev = 10
    for i in range(5, 10):
        theta = asin(sin(m)/10 * i)
        dy = cos(theta)
        dx = sin(theta)
        tx += 10/dy * dx
        t += 10/(dy*i)
    
    if tx > x:
        r = m
    else:
        l = m

print("{:.10f}".format(t))