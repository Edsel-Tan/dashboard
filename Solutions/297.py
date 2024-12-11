from prime import memoize
n = 10**17

fib = [0, 1, 2]
while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])

@memoize
def f(n):
    if n < 4:
        return n
    
    for i in range(len(fib)):
        if fib[i] > n:
            break

    output = n + f(n-fib[i-1])
    for j in range(1, i):
        output += f(fib[j] - fib[j-1] - 1)
    
    return output


print(f(10**17-1))