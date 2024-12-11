from fractions import Fraction # type: ignore
import math

def comp(i, a, number):
    index = 0
    while True:
        number, t = cf[i][number][0], cf[i][number][1]
        if index >= len(a):
            if index%2 == 1:
                return False
            else:
                return True
        else:
            #if t != a[-(k+1)]:
            if a[-(index+1)] < t:
                if index%2 == 0:
                    return False
                else:
                    return True
            if a[-(index+1)] > t:
                if index%2 == 0:
                    return True
                else:
                    return False
        index += 1
                
                
                
            
    

limit = 10**12
n = 10**5

cf = {}
for i in range(1, n+1):
    if math.isqrt(i)**2 == i:
        continue
    seq = {}
    number = (Fraction(0,1), Fraction(1))

    while number not in seq.keys():
        m = math.floor(number[0] + number[1] * math.sqrt(i))
        x = (number[0]-m)/((number[0] - m)**2 - i * number[1]**2)
        y = -number[1]/((number[0] - m)**2 - i * number[1]**2)
        if x < 0:
            x = -x
            y = -y
        seq[number] = [(x,y),m]
        number = (x,y)
    cf[i] = seq

output = 0
ans = []
for i in cf.keys():
    number = (Fraction(0,1), Fraction(1))
    nk, nkk = 1, 0
    dk, dkk = 0, 1
    alist = []

    while dk < limit:

        a = cf[i][number][1]
        alist.append(a)

        d = a*dk + dkk
        n = a*nk + nkk

        #print(n, d)


        if d < limit:
            dk, dkk = d, dk
            nk, nkk = n, nk

        else:
            if a % 2 == 0:
                if comp(i, alist[1:], number):
                    t = a//2
                else:
                    t = a//2 + 1
            else:
                t = a//2 + 1

            for j in range(a, t-1, -1):
                d = j*dk + dkk
                n = j*nk + nkk

                if d < limit:
                    dk, dkk = d, dk
                    nk, nkk = n, nk
                    break

            output += dk
            ans.append(dk)
            break

            
        number = cf[i][number][0]

print(output)
