import math
n=10**8

#b=0
o = n ** 2
for i in range(1,n+1):
    o -= n%i
    
o += (n//2) ** 2 * 2
for i in range(1,n//2 + 1):
    o -= 2 * ((n//2)%i)


for i in range(1,math.isqrt(n)+1):
    for j in range(i+1, math.isqrt(n-i**2)+1):
        if math.gcd(i,j) == 1:
            
            m = n//(i**2+j**2)
            for k in range(1,m+1):
                o += m//k * k * (i+j) * 2

print(o)
    
        
        
