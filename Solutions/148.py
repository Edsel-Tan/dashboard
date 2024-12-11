rows = 10**9

def numberToBase(n : int, base : int = 7):
    output = []
    while n > 0:
        output.append(n%base)
        n = n // base
    return list(reversed(output))

cache = {0:1}
def countInt(n : int):
    if n in cache:
        return cache[n]
    else:
        cache[n] = countInt(n-1) * 28
        return cache[n]

def count(nBaseSeven : list):
    if len(nBaseSeven) == 0:
        return 0
    else:
        return count(nBaseSeven[1:]) * (nBaseSeven[0] + 1) + (nBaseSeven[0] * (nBaseSeven[0] + 1)) // 2 * countInt(len(nBaseSeven) - 1)
    
print(count(numberToBase(rows)))
    