from prime import memoize
mod = 1111124111

n = 10**5
fib = [0,1]

for i in range(n):
    fib.append((fib[-1] + fib[-2]) % mod)

coeff = [0 for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n//i + 1):
        coeff[j*i] += (1 if j % 2 else -1) * fib[j]
        coeff[j*i] %= mod

F = [1]

for i in range(1, n+1):
    x = 0
    for j in range(1, i+1):
        x += coeff[j] * F[i-j]
        x %= mod
    F.append(x)

print(F[n])