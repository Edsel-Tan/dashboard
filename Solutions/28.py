a = lambda x: (4*x**3 - x)//3
b = lambda x: (4*x**3 - 9*x**2 + 8*x)//3
c = lambda x: (4*x**3 - 6*x**2 + 5*x)//3
d = lambda x: (4*x**3 - 3*x**2 + 2*x)//3

n = 1001
m = (n+1)//2
print(a(m)+b(m)+c(m)+d(m)-3)