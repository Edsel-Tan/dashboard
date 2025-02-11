n = 10**6

def palindromic(n):
    bn = bin(n)[2:]
    n = str(n)
    return n == "".join(reversed(n)) and bn == "".join(reversed(bn))


ans = 0
for i in range(1, n):
    if palindromic(i):
        ans += i
print(ans)