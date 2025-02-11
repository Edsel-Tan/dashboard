l = 10**10
f = lambda x: (x*(x+1))//2
g = lambda x: (x*(3*x-1))//2
k = lambda x: x*(2*x-1)

fs = set()
fg = set()
fk = set()

for i in range(1,l):
    if f(i) > l:
        break
    fs.add(f(i))
for i in range(1, l):
    if g(i) > l:
        break
    fg.add(g(i))
for i in range(1, l):
    if k(i) > l:
        break
    fk.add(k(i))
print(sorted(fs.intersection(fg).intersection(fk))[2])