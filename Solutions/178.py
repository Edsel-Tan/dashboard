import time

n = 40

start = time.time()
state = [[0 for i in range(4)] for j in range(10)]

for i in range(1,9):
    state[i][0] = 1
state[0][1] = 1
state[9][2] = 1

ans = 0

for _ in range(n-1):
    new_state = [[0 for i in range(4)] for j in range(10)]
    for i in range(1,9):
        for j in range(4):
            new_state[i][j] += state[i-1][j]
            new_state[i][j] += state[i+1][j]
    new_state[0][1] += state[1][0] + state[1][1]
    new_state[0][3] += state[1][2] + state[1][3]
    new_state[9][2] += state[8][2] + state[8][0]
    new_state[9][3] += state[8][1] + state[8][3]
    state = new_state

    for i in range(1,10):
        ans += state[i][3]
print(ans)