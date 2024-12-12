from math import acos, pi, sin, cos, sqrt, atan

def angle(a, b, c):
    return acos((a**2+b**2-c**2)/(2*a*b))

n = 10**6
l = 1.1033491
r = 1.1033493

best = 10**9
bx = 10**9


O = complex(0,0)

def spiral_center(a,b,c,d):
    return (b*c-a*d)/(b+c-a-d)

def polar_to_complex(r, t):
    return complex(r*cos(t), r*sin(t))

for i in range(n):
    x = l + i * (r-l) / n

    a,b,c = x**-1, x**(-8), x**(-7)
    
    t = 0
    A = polar_to_complex(1+a, t)
    t += angle(1+a, 1+b , a+b)
    B = polar_to_complex(1+b, t)
    t += angle(1+b, 1+c, b+c)
    C = polar_to_complex(1+c, t)

    P = spiral_center(A, B, O, C)
    
    tmp = (A-P)/(O-P)
    theta1 = atan(tmp.imag/tmp.real)

    tmp = (O-P)/(C-P)
    theta2 = (2 * pi - atan(tmp.imag/tmp.real))/7

    error = abs(theta2 - theta1)
    if error < best:
        best = error
        bx = x
        
        info = [theta1, 1/x, sqrt(P.imag**2+P.real**2)]

t,r,x = info[0], info[1], info[2]

r = bx
# r = 1.103349164825

def area(a,b,c):
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))

c0 = 1
c1 = r**-1
c8 = r**-8
c7 = r**-7


ta = area(c0+c7, c7+c8, c0+c8) + area(c0+c1, c1+c8, c0+c8)
tmp = [c0,c7,c8]
for i in range(3):
    a = tmp[i]
    b = tmp[(i+1)%3]
    c = tmp[(i+2)%3]
    ta -= (angle(a+b, b+c, c+a)) * b * b / 2

tmp = [c0,c1,c8]
for i in range(3):
    a = tmp[i]
    b = tmp[(i+1)%3]
    c = tmp[(i+2)%3]
    ta -= (angle(a+b, b+c, c+a)) * b * b / 2

ta *= r**2/(r**2-1)
print("{:.10f}".format(ta))


# ta = area(1,1,sqrt(2))
# tmp = [1-sqrt(2)/2, sqrt(2)/2, sqrt(2)/2]
# for i in range(3):
#     a = tmp[i]
#     b = tmp[(i+1)%3]
#     c = tmp[(i+2)%3]
#     ta -= angle(a+b, b+c, c+a) * b * b / 2

# print(ta)
# print(0.5-pi*(sqrt(2)/2)**2*0.25-pi*(1-sqrt(2)/2)**2*0.25)
# print(area(2,2,2), area(2,2,2) - pi/2)