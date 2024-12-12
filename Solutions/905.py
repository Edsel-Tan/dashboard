from prime import memoize

@memoize
def f(a,b,c):
    x,y,z = sorted([a,b,c])
    i,j,k = [[a,b,c].index(t) for t in [x,y,z]]
    if x == y:
        return k+1
    s = [0,0,0]
    s[k] = z % (2*x) if (z % (2*x) != 0) else 2*x
    s[j] = y % (2*x) if (y % (2*x) != 0) else 2*x
    s[i] = x
    n = (y - (y % (2*x) if (y % (2*x) != 0) else 2*x)) // (2*x) + (z -( z % (2*x) if (z % (2*x) != 0) else 2*x)) // (2*x)
    return f(*s) + ((k-j) % 3 if n % 2 == 1 else 0) + (n//2) * 3

ans = 0
for a in range(1,8):
    for b in range(1, 20):
        g = f(a**b, b**a, a**b + b**a)
        ans += g
print(ans)
    