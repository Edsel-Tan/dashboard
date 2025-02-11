def palindrome(x):
    return str(x) == ''.join(reversed(str(x)))

def f(x):
    return x + int(''.join(reversed(str(x))))

ans = 0
for i in range(1, 10001):
    j = i
    for _ in range(50):
        j = f(j)
        if palindrome(j):
            ans += 1
            break
print(10000-ans)