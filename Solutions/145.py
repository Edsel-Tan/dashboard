#output = 1
digits = 9
import itertools
fdigit = {0:0, 1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9,11:8,12:7,13:6,14:5,15:4,16:3,17:2,18:1}
digit = {0:1, 1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:9,11:8,12:7,13:6,14:5,15:4,16:3,17:2,18:1}

def check(lis, b):
    o = 0
    if lis[0] == 0:
        return 0

    if b % 2 == 0:

        for i in range(b//2):

            o += lis[i] * (10**i + 10**(b-1-i))

        while o > 0:

            if o%2 == 0:
                return 0
            else:
                o=o//10

        ans = fdigit[lis[0]]
        for i in lis[1:]:
            ans *= digit[i]

        #print(lis,b,ans)

        return ans

    else:

        for i in range(b//2+1):

            o += lis[i] * (10**i + 10**(b-1-i))


        while o > 0:

            if o%2 == 0:
                return 0
            else:
                o=o//10


        ans = fdigit[lis[0]]
        for i in lis[1:-1]:
            ans *= digit[i]

        #print(lis,b,ans)

        return ans

        
    
ans = 0
for i in range(1, digits+1):

    if i % 2 == 0:

        j = i//2

        for k in itertools.product([i for i in range(0,19)], repeat=j):
            ans += check(k, i)
            

    else:

        j = i//2

        for k in itertools.product([i for i in range(0,19)], repeat=j):
            for l in range(10):
                ans += check(k+(l,), i)

print(ans)