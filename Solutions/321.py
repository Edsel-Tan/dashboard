def next(x, y):
    return 3*x+4*y, 3*y+2*x

start = (5, 4)
solutions = []

for i in range(40):
    solutions.append((start[1]-2)//2)
    start = next(*start)

start = (11, 8)
for i in range(40):
    solutions.append((start[1]-2)//2)
    start = next(*start)

solutions = sorted(solutions)
print(sum(solutions[:40]))