letters = "AEFR"
keywords = ["FREE","FARE","AREA","REEF"]

state = {("", 0):1}
n = 30

def truncate(key):
    if len(key) >= 4:
        return key[1:]
    return key

for i in range(n):
    nstate = {}
    for j in state:
        a,b = j
        for l in letters:
            nkey = a+l
            if nkey in keywords:
                k = keywords.index(nkey)
                if b & (1 << k):
                    continue
                else:
                    key = (truncate(nkey), b | (1 << k))
                    if key in nstate:
                        nstate[key] += state[j]
                    else:
                        nstate[key] = state[j]
            else:
                key = (truncate(nkey), b)
                if key in nstate:
                    nstate[key] += state[j]
                else:
                    nstate[key] = state[j]

    state = nstate

ans = 0
for x,y in state:
    if y == 15:
        ans += state[(x,y)]
print(ans)