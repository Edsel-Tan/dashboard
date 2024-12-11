n = 1053779

import math

output = 0
for i in range(2, 3*n):
    for j in range(i//2 + 1, i):
        if math.gcd(i,j) != 1:
            continue
        a = 2*i*j - i*i
        b = 2*i*j - j*j
        c = i*i+j*j-i*j
        if a <= 0 or b <= 0 or c <= 0:
            continue
        g = math.gcd(a,b)
        a,b,c = a//g, b//g, c//g
        if (a+b-c > 12*n):
            break

        output += math.isqrt(12 * n * n //( (a + b - c) * (a + b - c)));

print(output)
        
    
