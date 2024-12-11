import itertools

def psums(lis):
    output = []
    for i in range(1,len(lis)+1):
        l = []
        for k in itertools.combinations([j for j in range(len(lis))],i):
            s = 0
            for m in k:
                s += lis[m]
            l.append(s)
        output.append(sorted(l))
    return output

def test(lis):
    s = psums(lis)
    for i in range(1, len(s)):
        if s[i][0] <= s[i-1][-1]:
            return False
        
    for i in s:
        if len(i) != len(set(i)):
            return False
    return True

print(20313839404245)