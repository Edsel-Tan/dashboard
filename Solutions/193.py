from prime import primes

t = 50
n = 2**t
p = primes(2**(t//2))
ans = 2**t

#PIE
counter = 1
def product(lis):
    output = 1
    for i in lis:
        output *= p[i] ** 2
    return output

lis = list(range(counter))
while product(lis) < n:

    l = product(lis)
    ans += ((-1) ** counter) * (n//l)

    while True:
        pointer = counter - 1
        while lis[pointer] == len(p) + pointer - counter and pointer >= 0:
            pointer -= 1
        if pointer == -1:
            break
        lis[pointer] += 1
        for i in range(pointer+1, counter):
            lis[i] = lis[i-1] + 1
        while product(lis) > n:
            pointer -= 1
            if pointer == -1:
                break
            lis[pointer] += 1
            for i in range(pointer+1, counter):
                lis[i] = lis[i-1] + 1

        if pointer == -1:
            break

        l = product(lis)
        ans += ((-1) ** counter) * (n//l)
        

        

    counter += 1
    lis = list(range(counter))

print(ans)