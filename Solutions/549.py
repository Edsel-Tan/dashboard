from prime import primes
n = 10**8

def vp(n, p):
    ans = 0
    x = p
    while x <= n:
        ans += n//x
        x *= p
    return ans

def least(p, e):
    left = 1
    right = n
    while right - left > 0:
        middle = (right + left)//2
        if vp(middle, p) >= e:
            right = middle
        else:
            left = middle+1
    return left

def main():

    isPrime = [True for i in range(n+1)]
    ans = [0 for i in range(n+1)]

    for i in range(2, n+1):
        if isPrime[i]:
            for k in range(i, n+1, i):
                isPrime[k] = False
            c = 1
            j = i
            k = j*i
            while (j <= n):
                y = least(i, c)
                for l in range(j, n+1, j):
                    if (l%k != 0):
                        ans[l] = max(ans[l], y)
                j *= i
                k *= i
                c += 1
    print(sum(ans))

main()