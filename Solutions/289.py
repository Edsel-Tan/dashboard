m = 6
n = 10

from prime import memoize
import itertools

validcrossings = []
def valid(crossing):
    if crossing[0] == 0 and crossing[1][0] in [0,2,3,7,10]:
        return False
    
    if crossing[-1] == 0 and crossing[1][-1] in [0,4,5,9,10]:
        return False
    
    for i in range(len(crossing[1])-1):
        if crossing[1][i] in [0,4,5,9,10] and crossing[1][i+1] in [0,2,3,7,10]:
            return False
        
    return True


temp = itertools.product(range(14), repeat = m-1)
for crossing in itertools.product(range(2), temp, range(2)):
    if valid(crossing):
        validcrossings.append(crossing)




def simplify(state):
    components = {}
    for i in range(len(state)):
        if state[i] not in components:
            components[state[i]] = len(components)
        state[i] = components[state[i]]
    return tuple(state)


@memoize
def transform(state):
    new_states = {}
    for crossings in validcrossings:
        valid, newstate = transformStateFromCrossing(state, crossings)
        if valid:
            if newstate in new_states:
                new_states[newstate] += 1
            else:
                new_states[newstate] = 1
    return new_states

def transformStateFromCrossing(state, crossings):
    newstate = [0 for i in state]
    info = {}
    componentLabel = dict(zip(set(state), set(state)))
    components = dict(zip(set(state), [set() for i in state]))
    for i in components:
        components[i].add(i)

    info["topEdge"] = 0
    info["bottomEdge"] = 1
    info["componentNumber"] = max(state) + 1
    info["i"] = 0

    def merge(x, y):
        x = componentLabel[x]
        y = componentLabel[y]
        z = min(x, y)
        for i in components[x]:
            componentLabel[i] = z
            components[z].add(i)
        for i in components[y]:
            components[z].add(i)
            componentLabel[i] = z

        del components[x+y-z]

    def addComponent():
        componentLabel[info["componentNumber"]] = info["componentNumber"]
        components[info["componentNumber"]] = set([info["componentNumber"]])
        info["componentNumber"] += 1

    if crossings[0]:
        newstate[0] = info["componentNumber"]
        info["topEdge"] = info["componentNumber"]
        addComponent()
        info["bottomEdge"] = state[0]
    
    else:
        newstate[0] = state[0]
        info["topEdge"] = info["componentNumber"]
        info["bottomEdge"] = info["componentNumber"]
        addComponent()
    


    def leftU():
        if componentLabel[info["bottomEdge"]] == componentLabel[info["topEdge"]]:
            return False
        
        merge(info["bottomEdge"], info["topEdge"])
        return True
        
    def topU():
        newstate[2*info["i"]+1] = info["componentNumber"]
        newstate[2*info["i"]+2] = info["componentNumber"]
        addComponent()
        return True


    def rightU():
        info["topEdge"] = info["componentNumber"]
        info["bottomEdge"] = info["componentNumber"]
        addComponent()
        return True
        

    def bottomU():
        if componentLabel[state[2*info["i"]+1]] == componentLabel[state[2*info["i"]+2]]:
            return False
        
        merge(state[2*info["i"]+1], state[2*info["i"]+2])
        return True

    def smallTopRightL():
        newstate[2*info["i"]+2] = info["componentNumber"]
        info["topEdge"] = info["componentNumber"]
        addComponent()
        return True

    def smallBottomRightL():
        info["bottomEdge"] = state[2*info["i"]+2]
        return True

    def smallBottomLeftL():
        if componentLabel[info["bottomEdge"]] == componentLabel[state[2*info["i"]+1]]:
            return False
        
        merge(info["bottomEdge"], state[2*info["i"]+1])
        return True

    def smallTopLeftL():
        newstate[2*info["i"]+1] = info["topEdge"]
        return True

    def bigTopLeftL():
        newstate[2*info["i"]+2] = info["bottomEdge"]
        return True

    def bigTopRightL():
        newstate[2*info["i"]+1] = info["componentNumber"]
        info["bottomEdge"] = info["componentNumber"]
        addComponent()
        return True
    
    def bigBottomRightL():
        info["topEdge"] = state[2*info["i"]+1]
        return True
    
    def bigBottomLeftL():
        if componentLabel[info["topEdge"]] == componentLabel[state[2*info["i"]+2]]:
            return False
        
        merge(info["topEdge"], state[2*info["i"]+2])
        return True
    
    def topStraightLine():
        return True
    
    def bottomStraightLine():
        return True
    
    def leftStraightLine():
        newstate[2*info["i"]+1] = state[2*info["i"]+1]
        return True

    def rightStraightLine():
        newstate[2*info["i"]+2] = state[2*info["i"]+2]
        return True
    
    for i, crossing in enumerate(crossings[1]):
        info["i"] = i
        
        if crossing == 0:

            if not leftU():
                return False, None
            if not topU():
                return False, None
            if not bottomU():
                return False, None
            if not rightU():
                return False, None

        elif crossing == 1:

            if not smallTopLeftL():
                return False, None
            if not smallBottomLeftL():
                return False, None
            if not smallTopRightL():
                return False, None
            if not smallBottomRightL():
                return False, None

        elif crossing == 2:

            if not leftU():
                return False, None
            if not bottomU():
                return False, None
            if not bigTopRightL():
                return False, None
            if not smallTopRightL():
                return False, None

        elif crossing == 3:

            if not leftU():
                return False, None
            if not topU():
                return False, None
            if not bigBottomRightL():
                return False, None
            if not smallBottomRightL():
                return False, None

        elif crossing == 4:

            if not bigBottomLeftL():
                return False, None
            if not smallBottomLeftL():
                return False, None
            if not topU():
                return False, None
            if not rightU():
                return False, None
        
        elif crossing == 5:

            if not smallTopLeftL():
                return False, None
            if not bigTopLeftL():
                return False, None
            if not bottomU():
                return False, None
            if not rightU():
                return False, None

        elif crossing == 6:

            if not smallTopLeftL():
                return False, None
            if not bottomStraightLine():
                return False, None
            if not bottomU():
                return False, None
            if not smallTopRightL():
                return False, None

        elif crossing == 7:

            if not leftU():
                return False, None
            if not leftStraightLine():
                return False, None
            if not smallTopRightL():
                return False, None
            if not smallBottomRightL():
                return False, None

        elif crossing == 8:

            if not topStraightLine():
                return False, None
            if not smallBottomLeftL():
                return False, None
            if not smallBottomRightL():
                return False, None
            if not topU():
                return False, None

        elif crossing == 9:

            if not smallTopLeftL():
                return False, None
            if not smallBottomLeftL():
                return False, None
            if not rightStraightLine():
                return False, None
            if not rightU():
                return False, None

        elif crossing == 10:

            if not leftU():
                return False, None
            if not leftStraightLine():
                return False, None
            if not rightStraightLine():
                return False, None
            if not rightU():
                return False, None

        elif crossing == 11:

            if not leftStraightLine():
                return False, None
            if not rightStraightLine():
                return False, None
            if not topU():
                return False, None
            if not bottomU():
                return False, None

        elif crossing == 12:

            if not bigBottomLeftL():
                return False, None
            if not smallBottomLeftL():
                return False, None
            if not bigTopRightL():
                return False, None
            if not smallTopRightL():
                return False, None

        elif crossing == 13:

            if not smallTopLeftL():
                return False, None
            if not bigTopLeftL():
                return False, None
            if not smallBottomRightL():
                return False, None
            if not bigBottomRightL():
                return False, None
            
    if crossings[2]:
        newstate[-1] = info["topEdge"]
        if componentLabel[info["bottomEdge"]] == componentLabel[state[-1]]:
            return False, None
        
        merge(info["bottomEdge"], state[-1])
    
    else:
        newstate[-1] = state[-1]
        if componentLabel[info["bottomEdge"]] == componentLabel[info["topEdge"]]:
            return False, None
        
        merge(info["bottomEdge"], info["topEdge"])

        

    return True, simplify([componentLabel[i] for i in newstate])




starting_states = []

for crossings in itertools.product(range(2), repeat = m-1):
    state = [0 for i in range(2*m)]
    componentNumber = 1
    currEdge = 0
    for edge in range(m-1):
        if crossings[edge]:
            #1 = _u_, 0 = T
            state[2*edge+1] = componentNumber
            state[2*edge+2] = componentNumber
            componentNumber += 1
        else:
            state[2*edge+1] = currEdge
            state[2*edge+2] = componentNumber
            currEdge = componentNumber
            componentNumber += 1
    state[2*m-1] = currEdge
    starting_states.append(simplify(state))


states = dict(zip([tuple(i) for i in starting_states], [1 for i in starting_states]))

mod = 10**10


for i in range(n-1):
    newstate = {}
    for i in states:
        r = transform(i)
        for j in r:
            if j in newstate:
                newstate[j] += r[j] * states[i]
            else:
                newstate[j] = r[j] * states[i]
            newstate[j] = newstate[j] % mod
    states = newstate

def validStateFromCrossing(state, crossing):

    componentLabel = dict(zip(set(state), set(state)))
    components = dict(zip(set(state), [set() for i in state]))
    for i in components:
        components[i].add(i)

    def merge(x, y):
        x = componentLabel[x]
        y = componentLabel[y]
        z = min(x, y)
        for i in components[x]:
            componentLabel[i] = z
            components[z].add(i)
        for i in components[y]:
            components[z].add(i)
            componentLabel[i] = z

        del components[x+y-z]

    currEdge = state[0]
    for edge in range(m-1):
        if crossing[edge]:
            if componentLabel[state[2*edge+1]] == componentLabel[state[2*edge+2]]:
                return False
            
            merge(state[2*edge+1], state[2*edge+2])
        
        else:
            if componentLabel[state[2*edge+1]] == componentLabel[currEdge]:
                return False
            
            merge(state[2*edge+1], currEdge)
            currEdge = state[2*edge+2]

    return True


ans = 0
for state in states:

    for crossing in itertools.product(range(2), repeat = m-1):

        if validStateFromCrossing(state, crossing):
            
            ans += states[state]
            ans = ans % mod

print(ans)

    
    


