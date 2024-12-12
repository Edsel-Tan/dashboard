from prime import memoize
m = 10**9+7

@memoize
def T(a, b):
    if b == 0:
        return H(a)
    if a == 0:
        return H(b)
    if a == 1 and b == 1:
        return 3
    
    output = 0
    for i in range(1, b+1):
        output += T(b-i, a) * pow(G(b, i), 6, m)
    return output % m
    

@memoize
def G(b, n):
    if n < 2 or b < 3:
        return 1
    
    states = {}
    for i in valid_states(b-2):
        states[i] = 1

    for i in range(n-2):
        nstates = {}
        for j in states.keys():
            for k in contract(j):
                if k in nstates:
                    nstates[k] += states[j]
                else:
                    nstates[k] = states[j]
        states = nstates

    # print(states)
    return sum(states.values()) % m


@memoize
def H(n):
    if n == 1:
        return 2
    states = {}
    for i in valid_states(n):
        states[i] = 1

    for i in range(n-1):
        nstates = {}
        # print(len(states), n)
        for j in states.keys():
            for k in expand(j):
                if k in nstates:
                    nstates[k] += states[j]
                else:
                    nstates[k] = states[j]
        states = nstates

    # print(len(states), n)

    for i in range(n-1):
        nstates = {}
        # print(len(states), n)
        for j in states.keys():
            for k in contract(j):
                if k in nstates:
                    nstates[k] += states[j]
                else:
                    nstates[k] = states[j]
        states = nstates

    return sum(states.values()) % m
    
import itertools
@memoize
def expand(state):
    output = []
    for i in valid_states(len(state)+1):
        # valid = True
        # for j in range(len(state)):
        #     if i[j] and i[j+1]:
        #         valid = False
        #         break
        if valid(i) and intersect(state, i):
            output.append(i)
    return output


@memoize
def contract(state):
    output = []
    for i in valid_states(len(state)-1):
        # valid = True
        # for j in range(len(state)-2):
        #     if i[j] and i[j+1]:
        #         valid = False
        #         break
        if valid(i) and intersect(i, state):
            output.append(i)
    return output

def intersect(state1, state2):
    for i in range(len(state1)):
        if state1[i] and (state2[i] or state2[i+1]):
            return False
    return True

@memoize
def valid(state):
    for j in range(len(state)-1):
        if state[j] and state[j+1]:
            return False
    return True

@memoize
def valid_states(n):
    output = []
    for i in itertools.product([0,1], repeat=n):
        if valid(i):
            output.append(i)
    return output


# t = 0
# for i in itertools.product([0,1], repeat = 20):
#     if valid(i):
#         t += 1
# print(t)
# print(expand([0,0]))
# print(contract([0,1,0]))

def ans(n):
    return (T(n,n)*2)%m

print(ans(10))