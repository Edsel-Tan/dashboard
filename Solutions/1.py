n = 10**3-1
def t(n):
    return (n*(n+1))//2
print(t(n//3) * 3 + t(n//5) * 5 - t(n//15) * 15)