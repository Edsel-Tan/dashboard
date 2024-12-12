from prime import primes
import math
import time


n = 5*10**15
pr = primes(math.isqrt(n)+1)

#Recursively add contributions of p1^a1p2^a2 ...
#Index = index of list, k = curr value of k, cont = contribution of k

def gcdsum(index, k, cont):
    output = 0

    output += n//k * cont
    for i in range(index+1, len(pr)):
        p = pr[i]
        #Only have contribution when k * p**2 <= n
        if k * p**2 > n:
            break
        e = 2
        while p**e * k <= n:

            #Split cases on whether p divides e or e-1.

            if e%p == 0:
                output += gcdsum(i, k * p**e, cont * (p**e - p**(e-2)))
            elif e%p == 1:
                #0 contribution
                pass
            else:
                output += gcdsum(i, k*p**e, cont * (p**(e-1) - p**(e-2)))


            e += 1

    return output

print(gcdsum(-1, 1, 1) -1)
    

