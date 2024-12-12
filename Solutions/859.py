def memoize(f):
    cache = {}
    def g(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return g

@memoize
def calculateOE(n):
    if n == 0:
        return 0
    if n == 1:
        return -1
    
    if n % 2 == 1:
        return min(0, -1 + 2*calculateOE((n-1)//2))
    return max(0, 1 + 2*calculateOE((n-2)//2))

@memoize
def calculate(N, ps):
    if ps == 1:
        return {calculateOE(1)*N : 1}
    output = {}
    OE = calculateOE(ps)
    for i in range(N//ps + 1):
        result = calculate(N-i*ps, ps-1)
        for j in result.keys():
            key = j + OE * i
            if key in output:
                output[key] += result[j]
            else:
                output[key] = result[j]
    return output

r = calculate(300, 300)
# print("DONE!")
# print(r, sum(r.values()))
# for i in range(16):
#     print(i, calculateOE(i))
ans = 0
for i in r.keys():
    if i >= 0:
        ans += r[i]
print(ans)

