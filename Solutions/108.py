from prime import primes

import math

def solve(i,n,p,c=[]):
    #print(c)
    minn = math.inf
    minsol = None
    if i == 1:
        t = math.ceil((n-1)/2)
        return math.log(p[-1]) * t, c + [n]
    o = True
    if len(c) == 0:
        j = 1
    else:
        j = c[-1]
    while (j-2) ** i < n or o:
        o = False
        sol = solve(i-1, math.ceil(n/j), p[:-1], c+[j])
        if sol[0] + (j-1)//2 * math.log(p[-1]) < minn:
            minsol = sol[0] + (j-1)//2 * math.log(p[-1]), sol[1]
            minn = minsol[0]
        j += 2
    return minsol
        
        
    
    

p = primes(50)
n = 2*1000+1

k =  math.ceil(math.log(n, 3))
x,y = solve(k,n,p[:k])
output = 1
for i,j in enumerate(p[:k]):
    output *= j ** math.floor(((y[-i-1])/2))
print(output)
    
