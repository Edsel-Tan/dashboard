
n = 10000
mod = 10**9
s = [[0,0,0,0,0,0],[0,0,1,0,0,0]]

def e(a,b,k,t = True):
    if t:
        return (b-1) ** 2 - (a-1) ** 2
    else:
        return (k-b) ** 2 - (k-a) ** 2

for i in range(n):
    D = s[-1]
    E = [0 for i in range(6)]
    E[0] = D[2] + D[1]
    E[1] = 1 + D[3] + D[0]
    E[2] = 1 + D[0] + D[4]
    E[3] = D[1] + D[5]
    E[4] = D[5] + D[2]
    E[5] = 1 + D[4] + D[3]
    s.append([i%mod for i in E])

def en(n,k,a,b,c):
    output = e(b,a,k, False)
    output += e(a,b,k) * s[n][0]
    output += e(b,a,k, False) * s[n][1]
    output += e(a,c,k) * s[n][2]
    output += e(c,a,k, False) * s[n][3]
    output += e(b,c,k) * s[n][4]
    output += e(c,b,k, False) * s[n][5]
    return output % mod

output = 0
for i in range(1, n+1):
    output = (output + en(i, pow(10, i, mod), pow(3, i, mod), pow(6, i, mod), pow(9, i, mod)))
print(output % 10**9)