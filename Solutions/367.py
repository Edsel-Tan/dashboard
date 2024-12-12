import itertools

n = 11

def simplify(state):
    visited = set()
    output = []
    for i in state:
        if i not in visited:
            c = 0
            while i not in visited:
                visited.add(i)
                i = state[i]
                c += 1
            output.append(c)
    return tuple(sorted(output))

def transition(state):
    output = {}
    for i in itertools.combinations(range(n), 3):
        for j in itertools.permutations([state[k] for k in i]):
            s = list(state)
            for k in range(3):
                s[i[k]] = j[k]
            v = simplify(s)
            if v in output:
                output[v] += 1
            else:
                output[v] = 1
    return output

states = {}
transitions = {}
for i in itertools.permutations(range(n)):
    v = simplify(i)
    if v in states:
        states[v] += 1
    else:
        states[v] = 1
        transitions[v] = transition(i)

s = tuple([1 for i in range(n)])
transitions[s] = {s:1}

matrix = [[0 for i in range(len(states))] for i in range(len(states))]
c = dict(zip(states.keys(), range(len(states))))

for i in states:
    matrix[c[i]][c[i]] += 1
    t = sum(transitions[i].values())
    for j in transitions[i]:
        matrix[c[i]][c[j]] -= transitions[i][j]/t

v = [1 for i in range(len(states))]
v[c[s]] = 0

matrix[c[s]][c[s]] = 1


def add(p, q, r):
    for i in range(len(q)):
        p[i] += r * q[i]

for i in range(len(states)):
    for j in range(len(states)):
        if j != i:
            r = matrix[j][i] / matrix[i][i]
            add(matrix[j], matrix[i], -r)
            v[j] -= r * v[i]
        
t = sum(states.values())
ans = 0
for i in states:
    ans += states[i] / t * v[c[i]] / matrix[c[i]][c[i]]
print(round(ans), ans)