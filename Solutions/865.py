p = 998244353
t = pow(10, -1, p)

prime_rings = [1]
prime_rings_not_starting_with = [1]
ans = [1]

n = (10**4)//3
# n = 10

for i in range(1, n+1):
    ans.append(0)
    prime_rings_not_starting_with.append(0)
    prime_rings.append(0)

    for j in range(i):
        prime_rings[i] += 10*prime_rings_not_starting_with[j]*prime_rings_not_starting_with[i-1-j]
        # prime_rings[i] += 10 * prime_rings[j] // 10 * 9 * prime_rings[i-j-1] // 10 * 9
    prime_rings[i] = prime_rings[i] % p
    
    for j in range(1,i+1):
        prime_rings_not_starting_with[i] += prime_rings[j] * t * 9 * prime_rings_not_starting_with[i-j]
    prime_rings_not_starting_with[i] = prime_rings_not_starting_with[i] % p

    for j in range(1, i+1):
        ans[i] += prime_rings[j] * ans[i-j]
    ans[i] = ans[i] % p

# print(ans)
# print(prime_rings)
# print(prime_rings_not_starting_with)
# print(5576195181577716)
# print(5576195181577716%p)
print((sum(ans[1:]) * t * 9) % p)