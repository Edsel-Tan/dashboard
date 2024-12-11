import math

ans = 0
for i in range(432, 1001):
    ans += math.factorial(1000) // math.factorial(i) // math.factorial(1000-i)

print("{:.12f}".format(ans / 2**1000))