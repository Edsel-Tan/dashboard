def c(n, r):
    output = 1
    for i in range(r):
        output *= n-i
        output = output // (i+1)
    return output

def p(n):
    output = 0
    for i in range(1, n):
        output += c(n, i) - 1
    return output * c(26, n)

print(max([p(i) for i in range(1, 27)]))