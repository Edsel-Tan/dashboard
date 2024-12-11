import math

def f(x, y):
    return math.sqrt((x+y)**2 - (100-x-y)**2)

def calc(b):
    output = 0
    output += b[0] + b[-1]
    for i in range(1, len(b)):
        output += f(b[i-1], b[i])
    return output

ans = 0
balls = [i for i in range(30, 51)]

def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp

n = len(balls)

index = 1

ans = calc(balls)
swap(balls, 0, index)
nans = calc(balls)
while nans < ans:
    ans = nans
    swap(balls, 0, index)
    index += 1
    swap(balls, 0, index)
    nans = calc(balls)

swap(balls, 0, index)
swap(balls, 0, index-1)
balls = [34, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
for a in range(30, 51):
    for b in range(30, 51):
        if a == b:
            continue
        balls = [i for i in range(30, 51)]
        balls.remove(a)
        balls.remove(b)
        balls.insert(0, a)
        balls.append(b)
        if calc(balls) < ans:
            d = balls
            ans = calc(balls)
        

balls = [49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
print(round(calc(balls)*100))

