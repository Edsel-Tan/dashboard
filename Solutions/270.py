n = 30
m = 10**8

from prime import memoize

@memoize
def triangle(polygon):
    a, b = polygon
    if a <= 2 or b <= 2:
        return 1
    return triangle((a-1, b)) + triangle((a, b-1))


@memoize
def f(polygon):
    # print(polygon)
    if len(polygon) == 2:
        # print(triangle(polygon))
        return triangle(polygon)
    if len(polygon) < 2:
        print(1)
        return 1

    output = 0

    #adjacent sides
    #left
    npolygon = list(polygon)
    npolygon[0] -= 1
    if npolygon[0] == 1:
        output += f(tuple(npolygon[1:]))
    else:
        output += f(tuple(npolygon))
    
    #right
    npolygon = list(polygon)
    npolygon[-1] -= 1
    if npolygon[-1] == 1:
        output += f(tuple(npolygon[:-1]))
    else:
        output += f(tuple(npolygon))

    for j in range(1, len(polygon)-1):
        if j != 1:
            output += f(polygon[:j]) * f(polygon[j:])
        for k in range(1, polygon[j]-1):
            lpolygon = list(polygon[:j])
            lpolygon.append(k+1)
            rpolygon = list(polygon[j:])
            rpolygon[0] -= k
            output += f(tuple(lpolygon)) * f(tuple(rpolygon))
        
    # print(output % m)
    return output % m


ans = 0   
ans += f((n, n+1, n+1, n))
ans += f((n+1, n+1)) * f((n+1, n))
for i in range(1, n):
    ans += f((n+1, i+1)) * f((n-i+1, n+1, n))
for i in range(1, n):
    ans += f((n+1, n+1, i+1)) * f((n-i+1, n))
print(ans%m)
