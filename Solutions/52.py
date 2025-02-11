x = 0
while True:
    x += 1
    z = sorted(str(x))
    b = True
    for i in range(1, 7):
        if sorted(str(i*x)) != z:
            b = False
            break
    if not b:
        continue
    print(x)
    break