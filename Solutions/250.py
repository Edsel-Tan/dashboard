n = 250250
m = 10**16 

sums = dict(zip(range(250), [0 for i in range(250)]))
sums[0] = 1
for i in range(1, n+1):
    i = pow(i, i, 250)
    newsums = sums.copy()
    for j in sums.keys():
        k = (i + j) % 250 
        newsums[k] += sums[j]
        newsums[k] = newsums[k] % m
    sums = newsums

print(sums[0]-1)