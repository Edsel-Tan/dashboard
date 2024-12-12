state = [0 for _ in range(8)]
state[0] = 1

for i in range(20):
    nstate = [0 for _ in range(8)]
    for j in range(1,8):
        nstate[j] += state[j] * (70 - (7-j) * 10 - i) / (70-i)
        nstate[j] += state[j-1] * ((7-j+1) * 10) / (70-i)
    state = nstate

ans = 0
for i in range(8):
    ans += i * state[i]
print("{:.9f}".format(ans))
