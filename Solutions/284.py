def crt(a, b, x, y):
    return (y*pow(y,-1,b)*a + b*pow(b,-1,y)*x) % (b*y)

f = lambda x : str(x) if x < 10 else chr(ord('a') + x-10)

def base14(x):
    output = ""
    while x > 0:
        output = f(x%14) + output
        x = x//14
    return output


n = 10000
ans = 16
a = 4
b = 1
asum = 8
x = 3
y = 1
xsum = 7
p = 1
q = 1

for i in range(2, n+1):
    p *= 2
    q *= 7
    if a%2 == 0 and b%7==0:
        a = a//2
        b = b//7
    else:
        for j in range(1, 14):
            c = a+j*q
            d = b+j*p
            if c%2==0 and d%7==0:
                a = c//2
                b = d//7
                asum += j
                # print(j, a, b)
                break
        ans += asum

    if x%2 == 0 and y%7==0:
        x = x//2
        y = y//7
    else:
        for j in range(1, 14):
            c = x+j*q
            d = y+j*p
            if c%2==0 and d%7==0:
                x = c//2
                y = d//7
                xsum += j
                # print(j, x, y)
                break
        ans += xsum

    
print(base14(ans))