from math import sin, cos, pi, sqrt, ceil

def area(x,y,z):
    return (x[0]*y[1] + y[0]*z[1] + z[0]*x[1] - x[1]*y[0] - y[1]*z[0] - z[1]*x[0]) * 0.5

def dist(a,b):
    return sqrt((a[0]-b[0])**2 + (a[1] - b[1])**2)

larea = 1 - pi/4

l = (5*pi)/4
r = (3*pi)/2
eps = 1e-12
threshold = 0.001
threshold_area = threshold * larea

while (r-l > eps):
    m = (r+l)/2
    pt = (cos(m), sin(m))
    # concave_triangle = area((-1,-1),(0,-1),pt) - ((3*pi)/2 - m)/2 + area((0,0), pt, (0,-1))
    concave_triangle = 0.5 - area((-1,-1), pt, (0,0)) - ((3*pi)/2 - m)/2
    if concave_triangle > threshold_area:
        l = m
    else:
        r = m

base = pt[0] + 1
height = pt[1] + 1
print(ceil(base/height))