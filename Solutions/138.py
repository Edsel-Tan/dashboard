# Easy to show that b is even 
# Use formula for pythogoras thriplet
# b = 2xy, h = x^2 - y^2
# Simplify to (x-2y)^2 - 5y^2 = +-1
# Pell's

n = 12

def generateNextSolution(x : int, y : int):
    return 9*x+20*y, 4*x+9*y

def getBL(x : int, y : int):
    x = x + 2*y
    return 2*x*y, x**2+y**2

sols = []
sol = (2, 1)
for i in range(n//2+1):
    sols.append(getBL(sol[0], sol[1]))
    sol = generateNextSolution(sol[0], sol[1])

sol = (9, 4)
for i in range(n//2+1):
    sols.append(getBL(sol[0], sol[1]))
    sol = generateNextSolution(sol[0], sol[1])

sols = sorted(sols)
print(sum([i[1] for i in sols[:n]]))