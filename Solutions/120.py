n = 1000
ans = 0

for i in range(3, n+1):

    ans += ( ((i-2) if i%2==0 else i-1 )) * i

print(ans)