def increasing(x):
    return sorted(str(x)) == list(str(x))

def decreasing(x):
    return sorted(str(x), reverse=True) == list(str(x))

def bouncy(x):
    return not (increasing(x) or decreasing(x))

counter = 0
x = 1
while True: 
    counter += bouncy(x)
    if (counter / x == 0.99):
        break
    x += 1

print(x)