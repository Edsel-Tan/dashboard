def is_palindrome(n):
    return str(n)[::-1] == str(n)

ans = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i*j):
            ans = max(i*j, ans)

print(ans)