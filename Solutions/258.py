m = 20092010
n = 2000

def convolute(a, b):
    output = [0 for i in range(len(a)+len(b)-1)]
    for i in range(len(a)):
        for j in range(len(b)):
            output[i+j] += a[i] * b[j]
            output[i+j] = output[i+j] % m
    return output

def simplify(a):
    if len(a) <= n:
        return a
    output = [a[i] for i in range(n)]
    for i in range(n, len(a)):
        output[i-n] = (output[i-n] + a[i]) % m
        output[i-n+1] = (output[i-n+1] + a[i]) % m
    return output

curr = [0,1]
k = 10**18
ans = [1]
while k != 0:
    if k % 2 == 1:
        ans = convolute(curr, ans)
        ans = simplify(ans)
    k = k // 2
    curr = convolute(curr, curr)
    curr = simplify(curr)
print(sum(ans)%m)

