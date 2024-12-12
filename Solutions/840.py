from prime import primes

pr = 999676999

ad = {1:1}
n = 5*10**4
p = primes(n)

for i in p:
    ad[i] = 1

for i in range(2,n+1):

    if i in p:
        continue

    for j in p:

        if i%j == 0:

            ad[i] = j*ad[i//j] + i//j * ad[j]
            ad[i] = ad[i] % pr

            break


s = {1: {}}
ans = 0


for i in range(1, n+1):

    si = ad[i]
    s[i] = {i:ad[i]}

    for j in range(i//2,0,-1):

        if j > (i-j)//2:
            si += ad[j] * s[i-j][i-j]
            s[i][j] = si % pr

        else:

            si += ad[j] * s[i-j][j]
            del s[i-j][j]
            s[i][j] = si % pr


    ans += s[i][1]
    ans = ans%pr

    if i%2==0:
        del s[i//2]


print(ans)
