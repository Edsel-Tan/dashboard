from prime import memoize

@memoize
def transform(state):
    t = {}
    state = [list(i) for i in state]
    for j in range(2):
        for i in range(len(state[j])):
            if state[j][i] in t:
                state[j][i] = t[state[j][i]]
            else:
                t[state[j][i]] = len(t)
                state[j][i] = t[state[j][i]]
    return state

@memoize
def advance(s):
    s = [list(i) for i in s]
    output = {-1:{}, 0:{},1:{}}
    for i in range(10):
        state = [i.copy() for i in s]
        score = 0
        if i in state[0]:
            score += 1
            index = state[0].index(i)
            del state[0][index]
            state[0].insert(0, i)
        else:
            if len(state[0]) < 5:
                state[0].insert(0, i)
            else:
                del state[0][-1]
                state[0].insert(0, i)
        if i in state[1]:
            score -= 1
        else:
            if len(state[1]) < 5:
                state[1].append(i)
            else:
                del state[1][0]
                state[1].append(i)
        state = tuple([tuple(i) for i in state])
        state = transform(state)
        state = tuple([tuple(i) for i in state])
        if state in output[score]:
            output[score][state] += 1
        else:
            output[score][state] = 1
    return output



state = {0: {((),()) : 1}}
for _ in range(50):
    newstate = {}
    for i in state.keys():
        for j in state[i].keys():
            k = advance(j)
            for l in k.keys():
                for m in k[l].keys():
                    if l+i in newstate:
                        if m in newstate[l+i]:
                            newstate[l+i][m] += state[i][j] * k[l][m]
                        else:
                            newstate[l+i][m] = state[i][j] * k[l][m]
                    else:
                        newstate[l+i] = {m: state[i][j] * k[l][m]}
    state = newstate
    # print(state)

ans = 0
for i in state.keys():
    ans += abs(i) * sum(state[i].values())
    # s += sum(state[i].values())
print("{:.8f}".format(ans / 10**50))


        