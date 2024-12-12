from __future__ import annotations

q = 10**8 + 7

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
            output.append(row)

        for i in range(len(output)):
            for j in range(len(output[i])):
                output[i][j] = output[i][j] % q

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
        
#Enumerate all tilings
import itertools
valid_tilings = {}

def vl(d):
    layer = [[True for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(2):
            if d[i*2 + j]:
                if layer[i][j] and layer[i][j+1]:
                    layer[i][j] = False
                    layer[i][j+1] = False
                else:
                    return False
                
    for i in range(3):
        for j in range(2):
            if d[i*2 + j + 6]:
                if layer[j][i] and layer[j+1][i]:
                    layer[j][i] = False
                    layer[j+1][i] = False
                else:
                    return False
                
    flatten = []
    for i in range(3):
        for j in range(3):
            flatten.append(str(int(layer[i][j])))
        
    t = "".join(flatten)
    t = int(t,2)

    return t

r = set()
def mp(d):
    layer = [[0 for _ in range(3)] for _ in range(3)]
    d = [i for i in range(len(d)) if d[i]]
    for k in d:
        layer[k//3][k%3] = 1

    flatten = [[] for _ in range(8)]
    for i in range(3):
        for j in range(3):
            flatten[0].append(str(int(layer[i][j])))
            flatten[1].append(str(int(layer[j][2-i])))
            flatten[2].append(str(int(layer[2-i][2-j])))
            flatten[3].append(str(int(layer[2-j][i])))

            flatten[4].append(str(int(layer[2-i][j])))
            flatten[5].append(str(int(layer[2-j][2-i])))
            flatten[6].append(str(int(layer[i][2-j])))
            flatten[7].append(str(int(layer[j][i])))

    for i in range(8):
        t = "".join(flatten[i])
        t = int(t, 2)
        if t in r:
            break
    else:
        t = "".join(flatten[0])
        t = int(t, 2)
        r.add(t)

    o = "".join(flatten[0])
    o = int(o, 2)

    return o, t

t = {}
for i in itertools.product([0,1], repeat = 9):
    a, b = mp(i)
    t[a] = b

x = len(set(t.values()))
y = dict(zip(list(set(t.values())), [i for i in range(x)]))




for i in itertools.product([0,1], repeat = 12):
    tiling = vl(i)
    if tiling != False:
        if tiling in valid_tilings:
            valid_tilings[tiling] += 1
        else:
            valid_tilings[tiling] = 1



m = [[0 for _ in range(512)] for _ in range(512)]
v = [[0 for _ in range(512)]]
v[0][0] = 1


for tiling in valid_tilings:
    for i in range(512):
        if tiling & i == i:
            k = tiling ^ i
            m[i][k] += valid_tilings[tiling]

mm = [[0 for _ in range(x)] for _ in range(x)]
vv = [[0 for _ in range(x)]]
vv[0][0] = 1

d = [True for i in range(x)]

for i in range(512):
    if d[y[t[i]]]:
        d[y[t[i]]] = False
    else:
        continue

    for j in range(512):
        mm[y[t[i]]][y[t[j]]] += m[i][j]



m = mm
v = vv
    
m = Matrix(m)
v = Matrix(v).transpose()

for i in range(10000):
    m = m ** 10

r = (m*v).entries
print(r[0][0])
# print((m**2*v).entries)
# for i in range(512):
#     print(r[i], r[t[i]], i, t[i])






