fib = [1,2]
n = 4*10**6
while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
print(sum([i if i % 2 == 0 else 0 for i in fib[:-1]]))