fdigits = [(1,0),(1,0)]
edigits = [1,1]

def pandigital(n):
    return sorted(str(n)[:9]) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

count = 2
while True:
    count += 1
    diff = fdigits[-1][1] - fdigits[-2][1]
    new = 10**diff * fdigits[-1][0] + fdigits[-2][0]

    if new > 10**20:
        fdigits.append((new//10, fdigits[-2][1] +1))

    else:
        fdigits.append((new, fdigits[-2][1]))

    edigits.append((edigits[-1] + edigits[-2])%10**9)

    pf = pandigital(fdigits[-1][0])
    pe = pandigital(edigits[-1])

    del fdigits[0]
    del edigits[0]

    if pf and pe:
        print(count)
        break
