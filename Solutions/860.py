n = 9898
m = 989898989

f = [1]
for i in range(1, n+1):
    f.append((f[-1] * i) % m)
fi = []
for i in range(n+1):
    fi.append(pow(f[i], -1, m))

def arrangements(a, b, c, d):
    return (f[a+b+c+d] * fi[a] * fi[b] * fi[c] * fi[d]) % m

ans = 0
for a in range(n+1):
    for b in range(a+1):
        # if a + b > n:
        #     break
        # if a != b:
        #     continue
        if (a+b)%2 != 0:
            continue
        p = n - a - b
        if p % 2 == 0:
            x = p // 2 + 2 * (a-b) 
            y = p // 2 - 2 * (a-b)
            if y < 0:
                continue
            

        else:
            x = (p+1) // 2 + 2 * (a-b)
            y = (p-1) // 2 - 2 * (a-b)
            if y < 0:
                continue

        # print(a, b, x, y)
        

        if a == b:
            ans += arrangements(x, y, a, b)
            # print(a, b, x, y, arrangements(x, y, a, b))
        else:
            ans += 2 * arrangements(x, y, a, b)
            # print(a, b, x, y, 2 * arrangements(x, y, a, b))

print(ans % m)
import math
# print(arrangements(5,4,1,0))
# print((math.factorial(10)//math.factorial(5))//math.factorial(5))