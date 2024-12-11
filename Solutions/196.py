from prime import miller_rabin

a = 5678027
b = 7208785

def neighbors(n, i):
    start = (n*(n-1))//2 + 1
    count = 0
    ni = []
    if i == 0:
        for j in range(2):
            if miller_rabin(start-n+j+1):
                count += 1
                ni.append([n-1, i+j])
            if miller_rabin(start+n+j):
                count += 1
                ni.append([n+1, i+j])
    elif i == n-2:
        for j in range(2):
            if miller_rabin(start+n-2-n+j):
                count += 1
                ni.append([n-1, i-1+j])
        for j in range(3):
            if miller_rabin(start+n-2+n-1+j):
                count += 1
                ni.append([n+1, i-1+j])
    elif i == n-1:
        for j in range(1):
            if miller_rabin(start+n-1-n+j):
                count += 1
                ni.append([n-1, i-1+j])
        for j in range(3):
            if miller_rabin(start+n-1+n-1+j):
                count += 1
                ni.append([n+1, i-1+j])
    else:
        for j in range(3):
            if miller_rabin(start+i-n+j):
                count += 1
                ni.append([n-1, i-1+j])
            if miller_rabin(start+i+n-1+j):
                count += 1
                ni.append([n+1, i-1+j])


    return count, ni

def S(n):
    output = 0
    start = (n*(n-1))//2+1
    for i in range(n):
        if miller_rabin(start+i):
            c, ni = neighbors(n, i)
            # print(c)
            if c >= 2:
                output += start+i
            else:
                for j in ni:
                    cc, ni = neighbors(j[0], j[1])
                    if cc >= 2:
                        output += start+i
                        break
    return output


c, ni = neighbors(5,2)
print(S(a)+S(b))
