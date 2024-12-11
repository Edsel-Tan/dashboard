import itertools

pos_scores = []
for i in range(1,21):
    pos_scores.append(i)
    pos_scores.append(2*i)
    pos_scores.append(3*i)

pos_scores.append(25)
pos_scores.append(50)

scores_count = []
for i in range(121):
    scores_count.append(0)

scores_count[0] = 1

for i in itertools.combinations(pos_scores, 1):
    scores_count[sum(i)] += 1
    scores_count[2*sum(i)] += 1


for i in itertools.combinations(pos_scores, 2):
    scores_count[sum(i)] += 1

ans = 0

doubles = [2*i for i in range(1, 21)]
doubles.append(50)

for i in range(2, 100):
    for j in doubles:
        if i-j < 0:
            break
        else:
            ans += scores_count[i-j]
            ##print(i-j, scores_count[i-j])

print(ans)