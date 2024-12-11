from prime import miller_rabin
import itertools

x = 10
numbers = []
output = 0
for l in range(1,10):
    counter = x
    ans = 0
    while(ans == 0):
        for i in itertools.combinations([t for t in range(x)], x-counter):
            for j in itertools.product([0,1,2,3,4,5,6,7,8,9], repeat = x-counter):
                c = 0
                n = ""
                for k in range(x):
                    if k in i:
                        n += str(j[c])
                        c += 1
                    else:
                        n += str(l)
                if miller_rabin(int(n)) and int(n) >= 10**(x-1):
                    ans += int(n)
                    numbers.append(int(n))
        counter -= 1
        # break
    output += ans

ans = 0
counter = x-1
while ans == 0:
    for l in range(1,10):
        for i in itertools.combinations([t for t in range(x-1)], x - 1 - counter):
            for j in itertools.product([0,1,2,3,4,5,6,7,8,9], repeat = x - 1 - counter):
                n = str(l)
                c = 0
                for k in range(x-1):
                    if k in i:
                        n += str(j[c])
                        c += 1
                    else:
                        n += str(0)
                if miller_rabin(int(n)) and int(n) >= 10**(x-1):
                    ans += int(n)
                    numbers.append(int(n))
    counter -= 1

output += ans
                        
print(output)
"""
422782205512
458782205557
460782205554
"""