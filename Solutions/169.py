
def cache(f):
    cache = {}
    def g(x,y):
        if (x,y) in cache.keys():
            return cache[(x,y)]
        else:
            cache[(x,y)] = f(x,y)
            return cache[(x,y)]
    return g

def g(x):

    if x == 1:
        return 1
    if x == 0:
        return 1
    if x%2 == 0:
        return g(x/2 - 1) + g(x/2)
    return g((x-1)/2)

def f(y, forced):
    if not forced:

        chunk1 = y.find("0")

        if chunk1 == -1:
            return 1

        chunk0 = y[chunk1:].find("1")

        if chunk0 == -1:
            return 1 + (chunk1) * len(y[chunk1:])
        
        #print(y, chunk0, chunk1)
        return (1 + chunk1 * chunk0) * f(y[chunk1:][chunk0:], False) + chunk1 * f(y[chunk1:][chunk0:], True)

    else:

        chunk1 = y.find("0")

        if chunk1 == -1:
            return 0

        chunk0 = y[chunk1:].find("1")

        if chunk0 == -1:
            return len(y[chunk1:])
        #print(y, chunk0)
        return chunk0 * f(y[chunk1:][chunk0:], False) + f(y[chunk1:][chunk0:], True)
        
print(f(bin(10**25)[2:], False))

for i in range(1000):
    if not g(i) == f(bin(i)[2:], False):
        print(i)

