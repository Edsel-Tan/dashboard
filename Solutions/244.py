def moves(n):
    output = []
    if n%4 > 0:
        output.append('R')
    if n%4 < 3:
        output.append('L')
    if n//4 > 0:
        output.append('D')
    if n//4 < 3:
        output.append('U')
    return output

def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

m = 10**8+7
end = (2,1,0,1,
        1,0,1,0,
        0,1,0,1,
        1,0,1,0)

states = set()
stack2 = [[(2,0,1,1,
           0,0,1,1,
           0,0,1,1,
           0,0,1,1), 0]]
stack1 = []
ans = {}
d = {'L':1, 'R':-1, 'U':4, 'D':-4}

while len(stack2) > 0:
    stack1 = stack2
    stack2 = []

    ans1 = {}

    for i in stack1:
        if i[0] in ans:
            continue
        if i[0] in ans1:
            ans1[i[0]] += i[1]
        else:
            ans1[i[0]] = i[1]

        s = list(i[0])
        n = s.index(2)
        for j in moves(n):
            ns = s.copy()
            ncs = (i[1] * 243 + ord(j)) % m
            swap(ns, n, n+d[j])
            stack2.append([tuple(ns), ncs])
    
    for i in ans1:
        ans[i] = ans1[i]

print(ans[end])



