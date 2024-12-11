import math
import sys

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def circle(P, Q, R):
    a = P[0]**2 + P[1]**2
    b = P[0]
    c = 1
    d = Q[0]**2 + Q[1]**2
    e = Q[0]
    f = 1
    g = R[0]**2 + R[1]**2
    h = R[0]
    i = 1

    y = a*e*f - a*h*f - b*d*i + b*g*f + c*d*h - c*g*e
    b = P[1]
    e = Q[1]
    h = R[1]
    x = a*e*f - a*h*f - b*d*i + b*g*f + c*d*h - c*g*e
    a = P[0]
    d = Q[0]
    g = R[0]
    c = a*e*f - a*h*f - b*d*i + b*g*f + c*d*h - c*g*e
    x = x/c * (0.5)
    y = y/c * (-0.5)
    r = math.sqrt((x-P[0])**2 + (y-P[1])**2)
    return r

def distsq(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2


n = 100000
l = 0
r = 2*n

while r - l > 0.01:
    m = (l+r)/2

    t = math.acos((2*n**2 - m**2) / (2*n**2))
    area = n**2 * (t - math.sin(t))
    if area < n:
        l = m
    else:
        r = m

l = math.floor(r)
sols = []
for a in range(1,l+1,2):
    for b in range(a, l+1, 2):
        if a**2 + b**2 > r**2:
            break
        if math.gcd(a, b) != 1:
            continue
        
        mr = circle((0,b-1),(0,b),(a,0))
        f = lambda x: (-b * x) / a + b
        for i in range(1,a):
            p1 = (i, math.floor(f(i)))
            mr = max(mr, circle(p1,(0,b),(a,0)))

        if mr > n:
            continue


        x = (a * pow(2, -1, b))%b
        y = (a * (2*x-a) + b**2) // (2*b)

        if x < a/2:
            x += b
            y += a

        while dist((x,y), (0,b)) <= mr:
            x += b
            y += a


        p = set()

        while distsq((x,y), (0,b)) <= n**2:
            q = distsq((x,y), (0,b))
            p.add(q)
            x += b
            y += a
        
        if len(p) > 0:
            sols.append(p)


ans = 0
stack = [(1, sols)]

while len(stack) > 0:
    t = stack[-1]
    del stack[-1]

    if len(t[1]) == 0:
        continue
    elif len(t[1]) == 1:
        ans += t[0] * (len(t[1][0]) * (len(t[1][0]) + 1)) // 2

    else:
        q = []
        for i in range(1, len(t[1])):
            r = t[1][0].intersection(t[1][i])
            if len(r) > 0:
                q.append(r)
        stack.append((t[0], t[1][1:]))
        stack.append((-1 * t[0], q))
        ans += t[0] * (len(t[1][0]) * (len(t[1][0]) + 1)) // 2
    
print(ans)



