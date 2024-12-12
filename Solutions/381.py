from prime import primes
n = 10**8

def main():
    p = primes(n)[2:]

    ans = 0
    for i in p:
        a = -1
        b = -1
        for j in range(2, 6):
            a *= pow(-j+1, -1, i)
            b += a
        ans += b%i
    print(ans)

main()