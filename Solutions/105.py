with open("0105_sets.txt", "r") as file:
    lines = file.readlines()

lines = [sorted([int(j) for j in i.strip("\n").split(",")]) for i in lines]

def check(s):
    for i in range(1, len(s)):
        if sum(s[-i:]) >= sum(s[:i+1]):
            return False
    t = [0]
    for i in s:
        t_ = t.copy()
        for j in t:
            if j + i in t:
                return False
            else:
                t_.append(j+i)
        t = t_
                
                
    return True

o = 0
for i in lines:
    if check(i):
        o += sum(i)
print(o)
