def LIS(lis : list[int]):
    inc = []
    for i in lis:
        if len(inc) == 0:
            inc.append(i)
            continue

        l = 0
        r = len(inc)

        while r-l:
            m = (r+l)//2
            if inc[m] <= i:
                l = m+1
            else:
                r = m
        
        if l == len(inc):
            inc.append(i)
            continue
        
        inc[l] = i
    
    return len(inc)

def S(n):
    s = set()
    pts = []
    for i in range(2*n):
        key = (pow(2, i, n), pow(3, i, n))
        if key in s:
            continue
        s.add(key)
        pts.append(key)
    pts = sorted(pts)
    npts = []
    for x,y in pts:
        npts.append(y)
    return LIS(npts)

def cS(n):
    result = S(n**5)
    return result

import multiprocessing

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        results = pool.map(cS, range(1, 31))

    
    print(sum(results))
