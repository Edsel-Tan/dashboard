dp = [[0 for i in range(50)] for j in range(50)]

for i in range(50):
    dp[0][i] = i
    dp[i][0] = i
i,j = 1,1
for i in range(1,50):
    for j in range(1,50):
        count = 0
        squares = [(0.5, i) for i in range(1, j+1)]
        for sq in squares:
            x,y = sq[0], sq[1]
            t = 500
            while x < i+1 and y < j+1:
                t = min(y//0.5, (i+1-x)//0.5, t)
                count += t
                #print(t,y,x)
                x += 0.5
                y += 0.5

        squares = [(1, 0.5+i) for i in range(j+1)]
        for sq in squares:
            x,y = sq[0], sq[1]
            t = 500
            while x < i+1 and y < j+1:
                t = min(y//0.5, (i+1-x)//0.5, t)
                count += t
                #print(t)
                x += 0.5
                y += 0.5

        dp[i][j] = int(count + dp[i-1][j])
            

output = 0
for i in range(47):
    for j in range(43):
        output += ((i+2)*(i+1))//2*((j+2)*(j+1))//2
        output += dp[i][j]
print(output)