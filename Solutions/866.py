from prime import memoize

m = 987654319

@memoize
def E(x):
    if x == 0:
        return 1
    output = 0
    for i in range(x):
        output += (E(i) * E(x-1-i) * x*(2*x-1)) // x
    return output % m

print(E(100))