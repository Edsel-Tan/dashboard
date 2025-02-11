from math import factorial

def f(n, k):
    if n == 1:
        return [0]
    output = []
    nf = factorial(n-1)
    output.append(k//nf)
    for i in f(n-1, k-k//nf*nf):
        if i >= output[0]:
            output.append(i+1)
        else:
            output.append(i)
    return output

n = 10
k = 10**6-1
print("".join([str(i) for i in f(n, k)]))