n = 23416728348467685

from prime import memoize

@memoize
def h(x):
    if x <= 0:
        return 0
    if x <= 3:
        return (x*(x+1))//2
    
    l = 1
    r = 2
    ans = 0

    while l <= x:
        ans += l
        ans += h(min(r, x+1)-l-1)
        t = r
        r = r + l
        l = t

    return ans

print(h(n))
        
        
        
    
