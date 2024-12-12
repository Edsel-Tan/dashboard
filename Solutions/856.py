from prime import memoize

@memoize
def E(state):
    mutable_state = list(state)
    num_of_cards = 0
    for i in range(1,5):
        num_of_cards += state[i] * i
    if num_of_cards == 0:
        return 0
    expected = 0
    for i in range(1,5):
        if state[i]:
            if i == state[5]:
                expected += (i) / num_of_cards
                mutable_state[i] -= 1
                mutable_state[i-1] += 1
                mutable_state[5] = i-1
                expected += ((state[i] - 1) * i) / num_of_cards * (E(tuple(mutable_state))+1)
                mutable_state[i] += 1
                mutable_state[i-1] -= 1
            else:
                mutable_state[i] -= 1
                mutable_state[i-1] += 1
                mutable_state[5] = i-1
                expected += (state[i] * i) / num_of_cards * (E(tuple(mutable_state))+1)
                mutable_state[i] += 1
                mutable_state[i-1] -= 1
    return expected

start = (0,0,0,0,13,-1)
print(f"{E(start):.8f}")
