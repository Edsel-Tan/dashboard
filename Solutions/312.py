# C(n) = 2 ^ (3 ^ n) x 3 ^ ((3^n - 3)/2)
# horrible garbage

def crt(a,b,x,y):
    return (b*x*pow(b,-1,y)+y*a*pow(y,-1,b))%(b*y),b*y

def crt_list(x, y):
    a,b = x[0], y[0]
    for i in range(1, len(x)):
        a,b = crt(a,b,x[i],y[i])
    return a

n = 10000

a1 = (n-2) % (12 * 13**2)
a2 = pow(3, a1, 13**3)

a3 = crt_list([0,1,a2],[3,8,13**3])
a4 = (a3-3)//2

z_2 = pow(2,a3,13**4) * pow(3,a4,13**4) - 2

a5 = crt_list([1,-1,z_2],[3,8,13**4])
a6 = pow(3,a5,13**5)

a7 = crt_list([0,1,a6],[3,8,13**5])
a8 = (a7-3)//2

y_2 = pow(2,a7,13**6) * pow(3,a8,13**6) - 2

a9 = crt_list([1,-2,y_2],[3,8,13**6])
a10 = pow(3,a9,13**7)

a11 = crt_list([0,1,a10],[3,8,13**7])
a12 = (a11-3)//2

x = pow(2,a11,13**8) * pow(3,a12,13**8)
print(x%(13**8))
