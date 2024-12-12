from __future__ import annotations

m = 10**8

class Matrix:

    def __init__(self, entries : list):
        self.entries = entries

    def transpose(self):
        output = [[0 for j in self.entries] for i in self.entries[0]]
        for i in range(len(self.entries)):
            for j in range(len(self.entries[0])):
                output[j][i] = self.entries[i][j]
        return Matrix(output)

    def __mul__(self : Matrix, other : Matrix):
        output = []
        other_transpose = other.transpose()
        for i in self.entries:
            row = []
            for j in other_transpose.entries:
                row.append(0)
                for k in range(len(j)):
                    row[-1] += i[k] * j[k]
                row[-1] = row[-1] % m
            output.append(row)

        return Matrix(output)
    
    def __pow__(self, exp : int):
        if exp == 0:
            output = [[0 for i in self.entries] for j in self.entries]
            for i in range(len(self.entries)):
                output[i][i] = 1
            return Matrix(output)
        
        if exp % 2 == 0:
            return (self * self) ** (exp//2)
        else:
            return (self * self) ** (exp//2) * self

e = 987654321
ans = 0
for n in range(1, 31):
    M = [[2**n,0,-n],[1,0,0],[0,1,0]]
    M = Matrix(M)
    # print((M*M).entries, M.entries)
    v = [[2**(2*n)],[2**n],[3]]
    v = Matrix(v)
    r = M**e * v
    ans += r.entries[2][0] - 1
    # print(r.entries)
print(ans%m)

# import math
# p = (1+math.sqrt(5))/2
# print(math.floor(p), math.floor(p**2), math.floor(p**3), math.floor(p**4))
# q = (1-math.sqrt(5))/2
# print(math.floor(p+q+1), math.floor(p**2+q**2+1), math.floor(p**3+q**3+1), math.floor(p**4+q**4+1))
