from prime import primes
n = 51

p = primes(n)
fmodp = []

for i in p:
    f = [0]
    for j in range(1, n+1):
        f.append(f[-1])
        while j % i == 0:
            f[-1] += 1
            j = j // i
    fmodp.append(f)

def choose(n, r):
    output = 1
    for i in range(r):
        output *= n-i
        output = output//(i+1)
    return output

sols = set()

for i in range(n):
    for j in range(i+1):
        b = True
        for k in range(len(p)):
            if fmodp[k][i] - fmodp[k][j] - fmodp[k][i-j] > 1:
                b = False
                break

        if b:
            sols.add(choose(i, j))

print(sum(sols))