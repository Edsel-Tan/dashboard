"""
Possible states:
2112 2002 0022 2200 2211 1122 0220

statetransitions
2112 -> 2112 0022 2200 0000
2002 -> 2112 0022 2200 0220 0000
0022 -> 1122 2002
2200 -> 2211 2002
2211 -> 2002 2211
1122 -> 2002 1122
0220 -> 2002
"""
m = 10**8
start = [[0],[1],[0],[0],[0],[0],[0]]

matrix = [[1,1,0,0,0,0,0],
          [0,0,1,1,1,1,1],
          [1,1,0,0,0,0,0],
          [1,1,0,0,0,0,0],
          [0,0,0,1,1,0,0],
          [0,0,1,0,0,1,0],
          [0,1,0,0,0,0,0]]

identity = [[0 for i in range(7)] for j in range(7)]
for i in range(7):
    identity[i][i] = 1

def multiply(a, b):
    output = []
    for i in a:
        output.append([])
        for j in range(len(b[0])):
            c = 0
            for k in range(len(i)):
                c += i[k] * b[k][j]
                c = c % m
            output[-1].append(c)
    return output

def T(n):
    n -= 1
    curr = [i.copy() for i in matrix]
    ans = [i.copy() for i in identity]

    while n != 0:
        if n % 2 == 1:
            ans = multiply(curr, ans)
        
        curr = multiply(curr, curr)
        n = n // 2

    ans = multiply(ans, start)
    
    return (sum(ans[0]) + sum(ans[1])) % m

print(T(10**12))
