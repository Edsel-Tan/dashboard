guesses = """5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct"""

g = guesses.split("\n")
n = 16

h = {}
f = {}
for i in g:
    j = i.split(";")
    h[j[0]] = int(j[1][0])

f = {}
for i in g:
    j = i.split(";")
    h[j[0]] = int(j[1][0])
    f[j[0]] = n - int(j[1][0])

def check(result):
    t = dict(zip(h.keys(), [0 for i in range(22)]))
    # print(t, h)
    for i in range(n):
        for j in h.keys():
            if result[i] == j[i]:
                t[j] += 1
    for i in h.keys():
        if h[i] != t[i]:
            return False
    return True


unsolved = []
def solve(state, info, result, active):
    b = True
    while b:
        b = False
        s = []
        ss = []
        for i in info.keys():
            if info[i] < 0:
                return False
            if info[i] == 0:
                s.append(i)
                for j in active:
                    try:
                        state[j].remove(i[j])
                    except:
                        pass

            

        for i in s:
            b = True
            # print(i)
            del info[i]


        s = []
        for i in active:
            if len(state[i]) == 0:
                return False
            if len(state[i]) == 1:
                # print(state[i], active)
                result[i] = state[i][0]
                s.append(i)
        
        for i in s:
            b = True
            del state[i]
            active.remove(i)
            for j in info.keys():
                if j[i] == result[i]:
                    info[j] -= 1

    m = None
    n = 3
    for i in info.keys():
        if info[i] < n:
            n = info[i]
            m = i

    if m:
        for i in active:
            if m[i] not in state[i]:
                continue
            newstate = dict(zip(state.keys(), [j.copy() for j in state.values()]))
            newinfo = info.copy()
            newresult = result.copy()
            newactive = active.copy()
            newactive.remove(i)
            newresult[i] = m[i]
            for j in newinfo.keys():
                if j[i] == newresult[i]:
                    newinfo[j] -= 1
            del newstate[i]
            
            if solve(newstate, newinfo, newresult, newactive):
                return True


    else:
        # print("FUCK!")
        # print(state, info, result, active)
        # unsolved.append((state, info, result, active))
        if len(active) == 0:
            if check(result):
                print("".join(result))
                return True

    

        
    return False

state = dict(zip([i for i in range(n)], [[str(j) for j in range(10)] for i in range(n)]))
result = [None for i in range(n)]
active = [i for i in range(16)]

solve(state, h.copy(), result, active)

