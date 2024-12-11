total = 1
states = {(1,0,0,0,0): 1}
from math import floor

ans = 0
for i in range(18):
    for state in states.keys():
        if sum(state) == 1:
            ans += states[state]
    
    new_states = {}
    for state in states.keys():
        s = sum(state)
        for i in range(5):
            if state[i] != 0:
                new_state = list(state)
                new_state[i] -= 1
                for j in range(i+1, 5):
                    new_state[j] += 1
                new_state = tuple(new_state)
                if new_state in new_states.keys():
                    new_states[new_state] += state[i] / s * states[state]
                else:
                    new_states[new_state] = state[i] / s * states[state]
    states = new_states

print("{:.6f}".format(ans-floor(ans)))
