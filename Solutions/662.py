a = 1
b = 2
s = set([1])

while b < 20000:
    s.add(b*b)
    b = a+b
    a = b-a

z = []

for x in range(10000):
    for y in range(10000):
        if x*x + y*y in s:
            z.append((x,y))

mod = 10**9+7
grid = [[0 for i in range(10001)] for j in range(10001)]
grid[0][0] = 1

for a in range(10001):
    for b in range(10001):
        for x,y in z:
            if a+x <= 10000 and b+y <= 10000:
                grid[a+x][b+y] = (grid[a+x][b+y] + grid[a][b]) % mod

print(grid[10000][10000])