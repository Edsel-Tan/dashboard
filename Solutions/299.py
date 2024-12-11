import math
from prime import primes
x = 10**8
rtx = math.isqrt(x)

#pythogorean case
ans = 0
for n in range(1, rtx+1):
    for m in range(n+1, x, 2):
        if math.gcd(m, n) != 1:
            continue
        a = m**2 - n**2
        b = 2 * m * n
        if a + b > x:
            break
        # print(a, b)
        ans += (x-1) // (a+b)
        
ans *= 2

def isSquare(n):
    return math.isqrt(n) ** 2 == n


def isSquare(n):
    return math.isqrt(n) ** 2 == n

# for a in range(1, x+1):
#     for b in range(a+1, x+1):
#         if math.gcd(a, b) != 1:
#             continue
#         if 2*(a + b + math.isqrt(2*a*b)) > x:
#             break
#         if isSquare(2*a*b):
#             print(a, b, (x-1)//(2*(a + b + math.isqrt(2*a*b))))
#             ans += (x-1)//(2*(a + b + math.isqrt(2*a*b)))

for a in range(1, rtx+1):
    if a%2 == 0:
        for b in range(math.isqrt(2*a**2)+1, x+1):
            if math.gcd(a, b) != 1:
                continue
            c = 2 * a * b
            if 2*(2*a**2 + b**2 + c) > x:
                break
            # print(2*a**2, b**2, (x-1)//(2*(2*a**2 + b**2 + c)))
            ans += (x-1)//(2*(2*a**2 + b**2 + c))
    else:
        for b in range(math.isqrt((a**2)//2)+1, x+1):
            if math.gcd(a, b) != 1:
                continue
            c = 2 * a * b
            if 2*(a**2 + 2*b**2 + c) > x:
                break
            # print(a**2, 2*b**2, (x-1)//(2*(a**2 + 2*b**2 + c)))
            ans += (x-1)//(2*(a**2 + 2*b**2 + c))
        for b in range(math.isqrt(2*a**2)+1, x+1):
            if math.gcd(2*a, b) != 1:
                continue
            c = 2 * a * b
            if 2*(2*a**2 + b**2 + c) > x:
                break
            # print(2*a**2, b**2, (x-1)//(2*(2*a**2 + b**2 + c)))
            ans += (x-1)//(2*(2*a**2 + b**2 + c))
        


print(ans)