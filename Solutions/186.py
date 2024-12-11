mod = 1000000
vtc = dict(zip([i for i in range(mod)],[i for i in range(mod)]))
vtcc = dict(zip([i for i in range(mod)],[[i] for i in range(mod)]))
S = [(100003 - 200003 * i + 300007 * i ** 3) % mod for i in range(1,56)]
counter = 0


#print("Done!")
up = 1

for j in range(27):
    a, b = S[2*j], S[2*j+1]

    if vtc[a] != vtc[b]:
        x = vtc[a]
        y = vtc[b]
        vtc[b] = x

        vtcc[x].extend(vtcc[y])
        del vtcc[y]

        for i in vtcc[x]:
            vtc[i] = x
    if a != b:
        counter += 1
    if up != len(vtcc[vtc[524287]]):
        up = len(vtcc[vtc[524287]])
        print(up)
    if len(vtcc[vtc[524287]]) > 0.99 * mod:
        print(counter)
            

a, b = S[54], (S[31] + S[0]) % mod

if vtc[a] != vtc[b]:
    x = vtc[a]
    y = vtc[b]
    vtc[b] = x

    vtcc[x].extend(vtcc[y])
    del vtcc[y]

    for i in vtcc[x]:
        vtc[i] = x

if a != b:
    counter += 1
if up != len(vtcc[vtc[524287]]):
    up = len(vtcc[vtc[524287]])

S[0] = b
index = 0

for j in range(10**8):
    S[(index+1)%55] = (S[(index-23)%55] + S[(index-54)%55])%mod
    S[(index+2)%55] = (S[(index-22)%55] + S[(index-53)%55])%mod
    a, b = S[(index+1)%55], S[(index+2)%55]
    index = (index + 2)%55
    #print(index)

    if vtc[a] != vtc[b]:
        x = vtc[a]
        y = vtc[b]
        if len(vtcc[y]) > len(vtcc[x]):
            x, y = y, x

        for i in vtcc[y]:
            vtc[i] = x

        vtcc[x].extend(vtcc[y])
##        if len(vtcc[x]) > 500000:
##            print(len(vtcc[x]))
        
        del vtcc[y]
    if a != b:
        counter += 1
    else:
        #print("z", j, a, b)
        #print(vtcc)
        pass
        #print("ZOOP", a, j)
    if up != len(vtcc[vtc[524287]]):
        up = len(vtcc[vtc[524287]])
    if len(vtcc[vtc[524287]]) >= 0.99 * mod:
        print(counter)
        break

