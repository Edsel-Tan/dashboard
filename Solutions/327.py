from prime import memoize

@memoize
def M(C, R):
    if C >= R+1:
        return R+1
    
    m = M(C, R-1)
    ans = C
    m -= C-1

    ans += m//(C-2) * C
    if m % (C-2) != 0:
        ans += m%(C-2) + 2

    return ans

ans = 0
for i in range(3, 41):
    ans += M(i, 30)
print(ans)