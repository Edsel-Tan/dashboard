p = 61
q = 10**7
m = 10
pp = 50515093

def NF(p, q):
    output = 0
    s = 290797
    t = s % p
    for i in range(m):
        output += t * pow(p, i, p**m)
        output = output % (p ** m)
        s = s ** 2
        s = s % pp
        t = s % p

    s = 290797
    t = s % p
    for i in range(q+1):
        output -= t
        output = output % (p ** m)
        s = s ** 2
        s = s % pp
        t = s % p

    return (output * pow(p-1, -1, p**m)) % p**m

print(NF(p, q))