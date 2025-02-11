ans = 0

def f(x):
    output = 0
    while x > 0:
        output += (x%10) ** 5
        x = x//10
    return output

for i in range(2, 10**6):
    if f(i) == i:
        ans += i
print(ans)