def memoize(f):
    cache = {}
    def g(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return g

triomino = [[(0,1), (0,2)], [(0,1), (1,0)], 
            [(0,1), (1,1)], [(1,0), (1,-1)],
            [(1,0), (2,0)], [(1,0), (1,1)]]

def place(state, pos, t):
    for d in t:
        if pos[0] + d[0] >= 0 and pos[0] + d[0] < len(state):
            if pos[1] + d[1] >= 0 and pos[1] + d[1] < len(state[pos[0] + d[0]]):
                if not state[(pos[0] + d[0])][(pos[1] + d[1])]:
                    return False
            else:
                return False
        else:
            return False
    return True

@memoize
def count(state : tuple) -> int:
    # print(state)
    output = 0
    state = [list(i) for i in state]
    # pos = (0, state[0].index(1))
    found = False
    x = 0
    while not found:
        try:
            y = state[x].index(1)
            found = True
        except:
            x += 1
        if x >= len(state):
            return 1
    pos = (x,y)
    for t in triomino:
        if place(state, pos, t):
            s = [i.copy() for i in state]
            s[pos[0]][pos[1]] = 0
            for i in t:
                s[pos[0]+i[0]][pos[1]+i[1]] = 0
            s = tuple([tuple(i) for i in s])
            output += count(s)
    return output

initial = tuple([tuple([1 for j in range(9)]) for i in range(12)])
print(count(initial))