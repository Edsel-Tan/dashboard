import math

with open("0107_network.txt", "r") as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] = [None if i == "-" else int(i) for i in data[i].strip("\n").split(",")]


cliques = dict(zip([i for i in range(len(data))], [i for i in range(len(data))]))
s = 0
for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j]:
            s += data[i][j]

s //= 2


def find_min(matrix):
    index = None
    min = math.inf
    for i in range(len(matrix)):
        for j in range((len(matrix))):
            if matrix[i][j]:
                if matrix[i][j] < min:
                    min = matrix[i][j]
                    index = (i,j)

    return min, index[0], index[1]

ans = 0
t = 0

while len(set(cliques.values())) != 1:
    minn, i, j = find_min(data)
    data[i][j] = None
    data[j][i] = None
    if cliques[i] != cliques[j]:
        for k in cliques.keys():
            if (cliques[k] == cliques[i] or cliques[k] == cliques[j]) and (k != i and k != j):
                cliques[k] = min(cliques[i], cliques[j])
        cliques[i] = min(cliques[i], cliques[j])
        cliques[j] = min(cliques[i], cliques[j])
        ans += minn
        t += 1

        
print(s-ans)