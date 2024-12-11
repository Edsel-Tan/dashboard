def is_palindrome(n):
    return str(n) == str(n)[::-1]

n = 10**8
import math
t = math.isqrt(n) + 1
sqs = [i ** 2 for i in range(1, t)]
c = 0
ans = []

while(sqs[c] + sqs[c+1] < n):
    curr = sqs[c] + sqs[c+1]
    i = 2

    while curr < n:
        if is_palindrome(curr) and curr not in ans:
            ans.append(curr)
        curr += sqs[c+i]
        i += 1
    
    c += 1

print(sum(ans))
