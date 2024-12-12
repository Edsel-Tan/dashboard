n = 2020
m = 10**16

ans = 0
for i in range(1, 10):
    dp = [0 for i in range(4*i+2)]
    dp[0] = 1

    sp = [0 for i in range(4*i+2)]

    for j in range(n):
        ndp = [0 for i in range(4*i+2)]
        nsp = [0 for i in range(4*i+2)]

        for k in range(0, 10):
            if k == i:
                for l in range(i+1):
                    ndp[l+2*i+1+k] += dp[l] + dp[l+2*i+1]
                    nsp[l+2*i+1+k] += sp[l] + sp[l+2*i+1] + (dp[l] + dp[l+2*i+1]) * pow(10,j,m) * k

            else:
                for l in range(2*i+1-k):
                    ndp[l+k] += dp[l]
                    ndp[l+k+2*i+1] += dp[l+2*i+1]
                    nsp[l+k] += sp[l] + (dp[l]) * pow(10,j,m) * k
                    nsp[l+k+2*i+1] += sp[l+2*i+1] + (dp[l+2*i+1]) * pow(10,j,m) * k

        
        for k in range(4*i+2):
            ndp[k] = ndp[k] % m

        dp = ndp
        sp = nsp
        # print(ndp, nsp)

    ans += nsp[-1]
    ans = ans % m

print(ans)
                    