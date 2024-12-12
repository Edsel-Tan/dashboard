from prime import memoize

@memoize
def a(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if (n%2 == 0):
        return 2 * a(n//2)
    return a(n//2) - 3 * a(n//2+1)

@memoize
def S(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 3
    return S(n//2) * 2 - 2 * (S((n+1)//2)) + 4 - a(((n+1)//2))

print(S(10**12))
