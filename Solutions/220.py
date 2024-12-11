from prime import memoize

def walk(x, y, o):
    if o == 0:
        return x, y
    if o == 1:
        return y, -x
    if o == 2:
        return -x, -y
    if o == 3:
        return -y, x

@memoize
def advance(order, steps):
    # print("Run", order, steps)
    if steps == 0:
        return 0,0,0
    
    if order == 0:
        return 0,1,0
    
    if order == 1:
        if steps == 1:
            return 0,1,0
        else:
            return 1,1,2
    
    x = 0
    y = 0
    o = 0
    c = 0
    while steps > 0:
        if order == 0:
            o = (o-1)%4
            a, b = walk(0, 1, o)
            # print(a, b, o)
            return x+a, y+b, o+1
        if c >= 2:
            o = (o+2)%4
        if steps > 2**(order-1):
            steps -= 2**(order-1)
            c+=1
            order -= 1
            # print(steps, order)
            a, b, d = advance(order, 2**order)
            a, b = walk(a, b, o)
            x += a
            y += b
            o = (o+d)%4
            # print(x, y, o)
        else:
            # print(x, y, o, c)
            a, b, d = advance(order-1, steps)
            a, b = walk(a, b, o)
            o += d
            return x+a, y+b, o

    return x,y,o

print(",".join([str(i) for i in advance(50,10**12)[:2]]))