import math

c = 1
while True:
    c += 1
    if c / math.floor(math.log2(c)) > 12345:
        break
print(c*(c+1))