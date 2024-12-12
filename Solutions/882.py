def statify(x):
    b = bin(x)[2:]
    c = 0
    output = []
    for i in range(len(b)):
        j = int(b[i])
        if j == 0:
            c += 1
            if c >= 0 and (i+1 == len(b) or b[i+1] == '1'):
                output.append(c)
                c = 0
        else:
            c -= 1
    return tuple(output)
        
def est(x):
    c = 0
    mc = 0
    for i in bin(x)[2:][::-1]:
        if i == '1':
            c -= 1
        else:
            c += 1
        mc = min(c, mc)
    return -mc


n = 100000
x = 0
st = {}
for i in range(1, n+1):
    x += est(i) * i
    y = statify(i)
    if y in st:
        st[y] += i
    else:
        st[y] = i
del st[()]
p = 1
s = 0
while len(st) > 0:
    n = max(st.keys())
    m = st[n]
    if m%2 == 0:
        a = b = m//2
    else:
        if p == 1:
            a = m//2+1
            b = m//2
        else:
            a = m//2
            b = m//2+1
        p = 1-p
    k = n[1:]
    if k in st:
        st[k] += a
    else:
        st[k] = a
    k = list(n)
    k[0] -= 1
    if k[0] == -1:
        k = k[1:]
        while len(k) > 0 and k[0] == 0:
            k = k[1:]
        if len(k) == 0:
            s += b
        else:
            k[0] -= 1
    k = tuple(k)
    if k in st:
        st[k] += b
    else:
        st[k] = b
    del st[n]
    if () in st:
        del st[()]
print(x+s+1-p)