n = 8
c = 3
import time

start = time.time()

def transform(row : list) -> list:
    colours = [i for i in range(c)]
    f = {}
    output = []
    for i in range(len(row)):
        if row[i] in f:
            output.append(f[row[i]])
        else:
            f[row[i]] = colours[0]
            del colours[0]
            output.append(f[row[i]])
    return output

# print(transform([2,1,0]))
def contract(state : dict) -> dict:
    output = {}
    for row in state.keys():
        possibilities = [[]]
        for i in range(len(row)-1):
            if row[i] != row[i+1]:
                for p in possibilities:
                    p.append((3 - row[i] - row[i+1])%3)
            else:
                newpos = []
                for p in possibilities:
                    q = p.copy()
                    q.append((row[i]+1)%3)
                    newpos.append(q)
                    q = p.copy()
                    q.append((row[i]+2)%3)
                    newpos.append(q)
                possibilities = newpos
        for p in possibilities:
            q = tuple(transform(p))
            if q in output:
                output[q] += state[row]
            else:
                output[q] = state[row]
    return output

def translate(state : dict) -> dict:
    output = {}
    for row in state.keys():
        possibilities = [[]]
        for i in range(len(row)):
            newpos = []
            for p in possibilities:
                q = p.copy()
                q.append((row[i]+1)%3)
                newpos.append(q)
                q = p.copy()
                q.append((row[i]+2)%3)
                newpos.append(q)
            possibilities = newpos
        for p in possibilities:
            q = tuple(transform(p))
            if q in output:
                output[q] += state[row]
            else:
                output[q] = state[row]
    return output

import itertools
state = {}
for i in itertools.product(range(3), repeat = n):
    j = tuple(transform(i))
    if j in state:
        state[j] += 1
    else:
        state[j] = 1

for i in range(n-1):
    state = contract(state)
    state = translate(state)
print(state[(0,)])







