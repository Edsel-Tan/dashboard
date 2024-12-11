from prime import primes
import math

def pfactors(n : int) -> list:
    output = []
    for pi in p:
        if n == 1:
            break
        if pi > math.isqrt(n):
            output.append(n)
            return output
        if n%pi == 0:
            output.append(pi)
            while n%pi == 0:
                n = n//pi
    return output


n = int(10**6 * 1.1)
p = primes(n)

ans = []
for pi in p:
    orderIsBig = True
    for pfi in pfactors(pi-1):
        if pow(10, (pi-1)//pfi, pi) == 1:
            orderIsBig = False
            break
    if orderIsBig:
        ans.append(pi)

for i in ans:
    if i > 10**6:
        answer = i
        break




def factors(n):
    output = [1]
    for pi in p:
        if n == 1:
            break
        if pi > math.isqrt(n):
            output.extend([n*i for i in output])
            break
        else:
            if n%pi == 0:
                exp = 0
                while n%pi == 0:
                    n = n//pi
                    exp += 1
                outputExtension = []
                for i in range(1, exp+1):
                    outputExtension.extend([pi**i * j for j in output])
                output.extend(outputExtension)
    return sorted(output)

def totient(n):
    output = 1
    for pi in p:
        if n == 1:
            break
        if pi > math.isqrt(n):
            output *= n-1
            break
        else:
            if n%pi == 0:
                output *= pi-1
                while n%pi == 0:
                    n = n//pi
    return output

def orderIsBig(n : int) -> bool:
    tn = totient(n)
    pfactorsOfN = pfactors(tn)
    if pow(10, tn, n) != 1:
        return False
    for pfi in pfactorsOfN:
        if pow(10, tn//pfi, n) == 1:
            return False
    return True


def order(n):
    factorsOfN = factors(totient(n))
    # print(len(factorsOfN))
    for factor in factorsOfN:
        if pow(10, factor, n) == 1:
            return factor
    return -1

# for i in range(int(0.8 * 10**6), answer+1):
#     if order(i) > 10**6:
#         print(i)

n = 10**6
a = []
for i in ans:
    if i%3 != 1:
        exp = math.ceil(math.log(n/i, 3))
        a.append(3**exp * i)
print(sorted(a)[0])


# for i in range(10**6, answer+1):
#     if orderIsBig(i):
#         print(i)

# print(pfactors(answer-1))
# print(order(answer))

# orderPrimes = {}
# for pi in p:
#     if pi == 2 or pi == 5:
#         continue
#     orderPrimes[pi] = order(pi)

# print(orderPrimes[:100])
            