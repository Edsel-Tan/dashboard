n = 10**7
k = 4*10**6
p = 10**9 + 7

f = [1]
fi = [1]

for i in range(1, n+10):
    f.append((f[-1] * i) % p)
    fi.append(pow(f[-1], -1, p))

def choose(n,r):
    return (f[n] * fi[r] * fi[n-r]) % p
        
output = 0
for i in range(k):
    output += choose(n+1,i) * pow(-1, i) * pow(k-i, n, p)
    output = output % p
print(output)
