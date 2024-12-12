from prime import segmented_sieve

n = 10**8
p = segmented_sieve(n)

def E(s):
    if len(s) == 0:
        return 0
    
    o = []
    e = []
    os = 0
    es = 0

    for i in s:
        if i < 2:
            if i % 2 == 1:
                os += 1
            else:
                es += 1
        
        else:
            if i % 2 == 1:
                o.append(i//2)
                os += 1
            else:
                e.append(i//2)
                es += 1


    return max(os, es) / (os + es) + len(o) / (os + es) * E(o) + len(e) / (os + es) * E(e)


print("{:.8f}".format(E(p)))