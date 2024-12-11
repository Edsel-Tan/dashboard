n = 11**12
m = 10**9
k = 23

def addX(A, B):
    return [(A[i] + B[i]) % m for i in range(k)]
    

def addXY(A, B):
    return [addX(A[i], B[i]) for i in range(k+1)]


def multX(A, B):
    output = [0 for i in range(k)]
    for i in range(k):
        for j in range(k):
            output[(i+j)%k] += A[i] * B[j]
            output[(i+j)%k] = output[(i+j)%k]
    return output


def multXY(A, B):
    output = [[0 for i in range(k)] for i in range(k+1)]
    for i in range(k+1):
        for j in range(k+1-i):
            output[(i+j)] = addX(multX(A[i], B[j]), output[(i+j)])
    return output

ans = [[0 for i in range(k)] for j in range(k+1)]
ans[0][0] = 1
for i in range(k-1):
    x = (n-i-1)//(k-1)+1

    t = [[0 for _ in range(k)] for _ in range(k+1)]
    for j in range(10):
        t[j][(pow(10, i, k)*j)%k] = 1

    
    while x > 0:
        if x % 2 == 1:
            ans = multXY(t, ans)
        t = multXY(t, t)
        x = x//2

print(ans[k][0])
