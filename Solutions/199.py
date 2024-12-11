import decimal # type: ignore
# from decimal import Decimal # type: ignore
# dec = Decimal
import math
# decimal.getcontext().prec = 16

# ccw = ((0, -1), (1, 0))
# cw = ((0, 1), (-1, 0))

def ccw(A):
    return (-A[1], A[0])

def cw(A):
    return (A[1], -A[0])

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
    return (x,y), r

def intersect(P, Q, r1, r2):
    a = r1 / (r1+r2)
    b = r2 / (r1+r2)
    return a * Q[0] + b * P[0], a * Q[1] + b * P[1]

def dist(P, Q):
    return math.sqrt((P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2)

def invert(P, Q):
    d = dist(P, Q)
    return (P[0] + 1/(d**2) * (Q[0] - P[0]), P[1] + 1/(d**2) * (Q[1] - P[1]))

def crossproduct(A, B):
    return A[0] * B[1] - A[1] * B[0] > 0

def plus(A, B):
    return (A[0] + B[0], A[1] + B[1])

def minus(A, B):
    return (A[0] - B[0], A[1] - B[1])

def invCircle(P, Q, R):
    Q_ = invert(P, Q)
    R_ = invert(P, R)
    M_ = intersect(Q_, R_, (0.5), (0.5))

    # print(Q_, R_, M_)

    if crossproduct(minus(Q_, M_), minus(P, M_)):
        v = cw(minus(Q_,M_))
    else:
        v = ccw(minus(Q_,M_))
    
    S_ = plus(M_, v)
    T_ = plus(S_, plus(v, minus(Q_, M_)))
    U_ = plus(S_, plus(v, minus(M_, Q_)))

    S = invert(P, S_)
    T = invert(P, T_)
    U = invert(P, U_)
    # print(S_, T_, U_)
    # print(S, T, U)
    return circle(T, U, S)

bigCircle = (((0),(0)), 2*math.sqrt((3))/3 + 1)
smallCircle = [(((0),(2*math.sqrt((3))/3)), (1)), (((1),-math.sqrt((3))/3), (1)), (((-1),-math.sqrt((3))/3), (1))]

bigCircleGaps = []
smallCircleGaps = [(smallCircle[0], smallCircle[1], smallCircle[2])]
allCircles = [bigCircle, smallCircle[0], smallCircle[1], smallCircle[2]]

# print(bigCircle)
# print(type(smallCircle[0][1]))

import itertools
for c1, c2 in itertools.combinations(smallCircle, 2):
    bigCircleGaps.append((bigCircle, c1, c2))

n = 10
for i in range(n):
    bCG = []
    sCG = []

    for bc, c1, c2 in bigCircleGaps:
        P = intersect(bc[0], c1[0], bc[1], -c1[1])
        Q = intersect(bc[0], c2[0], bc[1], -c2[1])
        R = intersect(c1[0], c2[0], c1[1], c2[1])

        c3 = invCircle(P, Q, R)
        allCircles.append(c3)
        # print(P, Q, R)
        # print(c3)
        bCG.append((bc, c1, c3))
        bCG.append((bc, c2, c3))
        sCG.append((c1, c2, c3))

    for c1, c2, c3 in smallCircleGaps:
        P = intersect(c1[0], c2[0], c1[1], c2[1])
        Q = intersect(c3[0], c2[0], c3[1], c2[1])
        R = intersect(c1[0], c3[0], c1[1], c3[1])

        c4 = invCircle(P, Q, R)
        # print(P, Q, R)
        # print(c4)
        allCircles.append(c4)
        sCG.append((c4, c1, c3))
        sCG.append((c4, c2, c3))
        sCG.append((c4, c2, c1))

    bigCircleGaps = bCG
    smallCircleGaps = sCG


def circleArea(c1):
    return (math.pi) * c1[1] ** 2


tarea = circleArea(bigCircle)
area = 0
for c in allCircles[1:]:
    area += circleArea(c)
print("{:.8f}".format(1- area/tarea))













# P = (dec(0), dec(0))
# Q = (dec(1), dec(0))
# R = (dec(0), dec(1))
# S = (dec(1), dec(1))

# print(invert(P, S))

# print(plus(Q, ccw(minus(P, Q))))

# print(circle(P, Q, R))

