import math

def memoize(f):
    cache = {}
    def g(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return g

@memoize
def count(n, d):
    if n == 0:
        return n == d
    a = len(str(n)) - 1
    a = 10**a
    b = n//a

    if b > d:
        return a + count(n-b*a, d) + count(a-1, d) * b
    if b == d:
        return n-b*a+1 + count(n-b*a, d) + count(a-1, d) * b
    
    return count(n-b*a, d) + count(a-1, d) * b


s = set()
def bscount(left, right, d):
    
    global s
    if right <= left:
        return
    m = (left+right) // 2
    mm = count(m, d)
    # print(left, right, d, m, mm)
    if mm < m:
        # print("ERE")
        bscount(m+1, right, d)

        explored = set()
        explored.add(m)
        while mm != m:
            if mm in explored:
                break
            m = mm
            explored.add(m)
            mm = count(m, d)
            if mm < left:
                return
            
        if mm == m:
            s.add(mm)
            bscount(left, mm, d)

    elif mm > m:
        # print("EHRE")
        # print(left, mm)
        bscount(left, m, d)

        explored = set()
        explored.add(m)
        while mm != m:
            if mm in explored:
                break
            m = mm
            explored.add(m)
            mm = count(m, d)
            if mm > right:
                return
            
        if mm == m:
            s.add(mm)
            bscount(mm, right, d)
    
    else:
        # print("EREH")
        tt = mm
        while tt == count(tt, d):
            # print("?")
            s.add(tt)
            tt -= 1
            if tt < left:
                return
        
        bscount(left, tt, d)

        tt = mm
        while tt == count(tt, d):
            # print("?")
            s.add(tt)
            tt += 1
            
            if tt > right:
                return
            
        bscount(tt, right, d)

bscount(0, 9999999999, 1)

ans = 0
for i in range(1, 10):
    s = set()
    bscount(0, 9999999999999999, i)
    bscount(0, 999999999999999, i)
    ans += sum(s)

print(ans)