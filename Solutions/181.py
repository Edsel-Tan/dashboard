import math

dp = []
p = []
partition = []

b = 60
w = 40

p.append([1])
for i in range(1, b+w+1):
    p.append([0])
    
    for j in range(1, i+1):
        p[i].append(p[i-1][j-1])
        if j <= i-j:
            p[i][j] += p[i-j][j]
        

for i in range(w+1):
    partition.append(sum(p[i]))



for i in range(b+1):
    dp.append([])

    for j in range(i+1):
        dp[i].append([])

        for k in range(w+1):
            dp[i][j].append(0)


dp[0][0] = partition
for i in range(1, b+1):
    
    for j in range(1, i+1):

        for k in range(w+1):

            for l in range(i//j + 1):
                
                for m in range(k+1):
                    dp[i][j][k] += dp[i-l*j][min(j-1, i-l*j)][k-m] * p[m+l][l]

#print(dp)
print(dp[b][b][w])


            


        

        
