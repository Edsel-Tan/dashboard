from math import cos, sin, pi, atan
f = lambda t,a: -9.81 * t * t / 2 + 20 * t * sin(a) + 100

dx = 1e-3
ans = 0
x = dx
while True:
    a = atan(400/(9.81*x))
    t = x/(20*cos(a))
    y = f(t,a)
    if y < 0:
        break
    ans += 2*pi*dx*x*y
    x += dx

print("{:.4f}".format(ans))