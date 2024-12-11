from fractions import Fraction # type: ignore


def memoize(f):
    cache = {}
    def g(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return g

def neighbors(x):
    output = []
    if x%5 > 0:
        output.append(x-1)
    if x%5 < 4:
        output.append(x+1)
    if x//5 > 0:
        output.append(x-5)
    if x//5 < 4:
        output.append(x+5)
    return output
    
def swap(M, i, j):
    temp = M[i]
    M[i] = M[j]
    M[j] = temp


def solveMatrix(M, x):
    for i in range(len(M)):
        if M[i][i] == 0:
            print("Fail")
        for j in range(len(M)):
            if j == i or M[j][i] == 0:
                continue
            c = M[j][i] / M[i][i]
            for k in range(len(M)):
                M[j][k] -= M[i][k] * c
            x[j] -= x[i] * c
    for i in range(len(M)):
        x[i] /= M[i][i]
    # print(M, x)
    return x




def createMatrix(goal, freeSquares):
    sqToVno = {}
    for i in range(20):
        sqToVno[i] = i
    for i in freeSquares:
        sqToVno[i] = len(sqToVno)
    
    output = [[0 for i in range(len(sqToVno))] for j in range(len(sqToVno))]
    v = [0 for i in range(len(sqToVno))]
    for i in sqToVno.keys():
        n = neighbors(i)
        inSTV = []
        for j in n:
            if j in sqToVno:
                inSTV.append(j)

        for j in inSTV:
            output[sqToVno[i]][sqToVno[j]] = -Fraction(1, len(n))

    goaln = neighbors(goal)
    goalninSTV = []

    for i in goaln:
        if i in sqToVno:
            goalninSTV.append(i)
    
    for i in goalninSTV:
        n = neighbors(i)

        # for j in inSTV:
        #     output[sqToVno[i]][sqToVno[j]] = -Fraction(1, len(n))
        
        v[sqToVno[i]] += Fraction(1, len(n))

    for i in range(len(sqToVno)):
        output[i][i] = 1

        
    return output, v

def createTMatrix(freeSquares):
    sqToVno = {}
    for i in range(25):
        sqToVno[i] = i
    
    output = [[0 for i in range(len(sqToVno))] for j in range(len(sqToVno))]
    v = [1 for i in range(len(sqToVno))]
    for i in range(25):
        if i not in freeSquares:
            n = neighbors(i)
            inSTV = []
            for j in n:
                if j in sqToVno:
                    inSTV.append(j)

            for j in inSTV:
                output[sqToVno[i]][sqToVno[j]] = -Fraction(1, len(n))

    for i in freeSquares:
        v[i] = 0

    for i in range(len(sqToVno)):
        output[i][i] = 1

        
    return output, v

def createEMatrix(goal, freeSquares):
    p = solveMatrix(*createMatrix(goal, freeSquares))

    sqToVno = {}
    for i in range(20):
        sqToVno[i] = i
    for i in freeSquares:
        sqToVno[i] = len(sqToVno)
    # sqToVno[goal] = len(sqToVno)
    
    output = [[0 for i in range(len(sqToVno))] for j in range(len(sqToVno))]
    v = [p[i] for i in range(len(sqToVno))]
    for i in sqToVno.keys():
        n = neighbors(i)
        inSTV = []
        for j in n:
            if j in sqToVno:
                inSTV.append(j)

        for j in inSTV:
            output[sqToVno[i]][sqToVno[j]] = -Fraction(1, len(n))

        # v[sqToVno[i]] = Fraction(len(inSTV), len(n))

    # v[sqToVno[goal]] = 0
    # for i in range(len(output)):
    #     output[sqToVno[goal]][i] = 0


    # goaln = neighbors(goal)
    # goalninSTV = []

    # for i in goaln:
    #     if i in sqToVno:
    #         goalninSTV.append(i)
    
    # for i in goalninSTV:
    #     n = neighbors(i)
    #     inSTV = []
    #     for j in n:
    #         if j in sqToVno:
    #             inSTV.append(j)

    #     for j in inSTV:
    #         output[sqToVno[i]][sqToVno[j]] = -Fraction(1, len(inSTV) + 1)
        
    #     # v[sqToVno[i]] += Fraction(1, len(n))

    for i in range(len(output)):
        output[i][i] = 1

    return output, v


# print(neighbors(0))
# m = createEMatrix(23, [24])
# for i in m[0]:
#     print(i)
# print(m[1])
# print([i.numerator/i.denominator for i in solveMatrix(*m)])

# print("------------------------")

# m = createMatrix(20, [])
# for i in m[0]:
#     print(i)
# print(m[1])
# print(solveMatrix(*m))

# t = 0
# for i in range(20, 24):
#     t += solveMatrix(*createEMatrix(i, (24,)))[1]
# print(t.numerator/t.denominator)

# t = solveMatrix(*createTMatrix((20,21,22,23)))[1]
# print(solveMatrix(*createTMatrix((20,21,22,23))))
# print(t.numerator/t.denominator)

cache = {}
ecache = {}
# """
import itertools
for i in range(5):
    for j in itertools.combinations([20,21,22,23,24], i):
        for k in range(20, 25):
            if k not in j:
                cache[(k, j)] = solveMatrix(*createMatrix(k, j))
                ecache[(k, j)] = solveMatrix(*createEMatrix(k, j))
        # print(j)

# test = 0
# for k in range(20, 24):
#     test += cache[(k, (24,))][1]
# print(test)

E = 0
totalP = 0
for l, u in itertools.product(itertools.permutations([0,1,2,3,4]), repeat=2):
    # print(l, u)
    lower = []
    upper = []
    start = 12
    e = 0
    p = 1
    for j in range(5):
        e += ecache[(l[j]+20, tuple(lower))][start] / cache[(l[j]+20, tuple(lower))][start]
        p *= cache[(l[j]+20, tuple(lower))][start]
        start = l[j]
        lower.append(l[j]+20)
        lower = sorted(lower)

        e += ecache[(u[j]+20, tuple(upper))][start] / cache[(u[j]+20, tuple(upper))][start]
        p *= cache[(u[j]+20, tuple(upper))][start]
        start = u[j]
        upper.append(u[j]+20)
        upper = sorted(upper)
    totalP += p
    E += e * p 
print("{:.6f}".format(E.numerator / E.denominator))

# """