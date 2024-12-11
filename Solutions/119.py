limit = 20
l = 10**20

output = []

def digsum(n):
    return sum([int(i) for i in list(str(n))])

for i in range(2, 9*limit):
    j = i

    while j < l:
        if j < 10:
            j *= i
        else:
            if digsum(j) == i:
                output.append(j)
            j *= i

print(sorted(output)[29])