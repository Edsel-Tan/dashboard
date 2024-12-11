import math

n = 10**5

ans = 0

for k in range(1, 2):
    a = 0
    x = 0

    h = ((2*k+1))/((2*k))
    y = math.sqrt(h**2 - 1/(k**2)) - 1/k
    theta = math.acos(1/(h*k)) - math.pi/4
    b = theta * (h**2) - (y-x) / k
    # print(h, y, theta, b)

    # print(x, y, theta, a, b, b-a)
    # print(b-a)

    ans += (b-a) * k


for k in range(2, n+1):
    h = ((2*k-1))/((2*k))
    x = math.sqrt(h**2 - 1/(k**2)) - 1/k
    theta = math.acos(1/(k*h)) - math.pi/4
    a = theta * (h ** 2)
    # print(h, x, theta, a)

    h = ((2*k+1))/((2*k))
    y = math.sqrt(h**2 - 1/(k**2)) - 1/k
    theta = math.acos(1/(h*k)) - math.pi/4
    b = theta * (h**2) - (y-x) / k
    # print(h, y, theta, b)

    # print(x, y, theta, a, b, b-a)
    # print(b-a)

    ans += (b-a) * k

print("{:.5f}".format(ans))