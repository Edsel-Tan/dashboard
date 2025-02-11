ans = set()
k = sorted("123456789")

for i in range(10,100):
    for j in range(100, 1000):
        if sorted(str(i) + str(j) + str(i*j)) == k:
            ans.add(i*j)

for i in range(1,10):
    for j in range(1000, 10000):
        if sorted(str(i) + str(j) + str(i*j)) == k:
            ans.add(i*j)

print(sum(ans))