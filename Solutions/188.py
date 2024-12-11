def totient(n):
    if n%2 == 0:
        n = n/2
    if n%5 == 0:
        n = n/5 * 4
    return int(n)

def tetration(a, b, mod):
    if b == 1:
        return a
    if mod == 1:
        return 0
    return pow(a, tetration(a, b-1, totient(mod)), mod)

print(tetration(1777,1855,10**8))