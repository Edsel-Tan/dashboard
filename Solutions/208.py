n = 70

states = {0: {(0,0,0,0,0):1}, 1: {}, 2:{}, 3: {}, 4: {}}

for i in range(n):
    newstate = {0 : {}, 1 : {}, 2 : {}, 3 : {}, 4 : {}}
    for j in range(5):
        for k in states[j].keys():
            l = list(k)
            l[j] += 1
            l = tuple(l)
            if l in newstate[(j-1)%5]:
                newstate[(j-1)%5][l] += states[j][k]
            else:
                newstate[(j-1)%5][l] = states[j][k]

            l = list(k)
            l[(j+1)%5] += 1
            l = tuple(l)
            if l in newstate[(j+1)%5]:
                newstate[(j+1)%5][l] += states[j][k]
            else:
                newstate[(j+1)%5][l] = states[j][k]
    states = newstate

m = n//5
print(states[0][(m,m,m,m,m)])