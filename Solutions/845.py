def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

p = primes1(10**3)
digit_sums = dict(zip([i for i in range(0,10)],[1 for i in range(0,10)]))

def add_digit(ds, digits):
    nds = ds.copy()
    for i in digits:
        for j in ds.keys():
            if j + i not in nds.keys():
                nds[j+i] = ds[j]
            else:
                nds[j+i] += ds[j]
    return nds

d = [i for i in range(1,10)]
def count(ds):
    output = 0 
    for i in ds.keys():
        if i in p:
            output += ds[i]
    return output


def count_but_good(n):
    t = len(str(n))-1
    output = 0
    s = 0
    for i in str(n):
        i = int(i)
        if t >= 1:
            if i - 1 == -1:
                t -= 1
                continue
            ds = dict(zip([i for i in range(s,s+10)],[1 for i in range(0,10)]))
            for k in range(t-1):
                ds = add_digit(ds, d)
            ds = add_digit(ds, [j for j in  range(1, i)])
            output += count(ds)

        else:
            ds = dict(zip([i for i in range(s,s+i+1)],[1 for i in range(0,i+1)]))
            output += count(ds)

        t -= 1
        s += i
    return output


upper = 10**17
lower = 0

while upper - lower > 1:
    mid = (upper + lower)//2
    if count_but_good(mid) > 10**16-1:
        upper = mid
    elif count_but_good(mid) < 10**16-1:
        lower = mid
    else:
        break

print(upper)
