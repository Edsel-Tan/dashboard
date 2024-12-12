mod = 10**9 + 7

# n = 3**8
# n = 3
# def xor_product(a, b):
#     ans = 0
#     while a > 0:
#         if a & 1:
#             ans = ans ^ b
#         b = b << 1
#         a = a >> 1
#     return ans

# def xor_exp(a, b):
#     ans = 1
#     while b > 0:
#         if b & 1:
#             ans = xor_product(ans, a)
#         a = xor_product(a, a)
#         b = b >> 1
#     return ans

# b = lambda x: bin(x)[2:]

# print(xor_exp(11, 48)%mod)

# k = 4
# s = []
# while n > 0:
#     if n & 1:
#         s.append(k)
#     k += 1
#     n = n >> 1

# print(xor_exp(11, 16)*xor_exp(11, 32))
# print(b(xor_exp(11, 16)))
# print(b(xor_exp(11, 32)))
# print(xor_product(xor_exp(11, 16),xor_exp(11, 32)))
# print(xor_exp(11, 48))

# print(s)
# ans = 1
# for i in s:
#     ans = (ans * (1 + pow(2, pow(2, i, mod-1), mod) + pow(2, 3*pow(2,i,mod-1), mod)))%mod

# print(ans)

n = 3**8
k = 52

terms = {(0,0):1,(1,0):1,(3,0):1}
def plus(a, b):
    return (a[0]+b[0], a[1]+b[1])

def xor_product(a, b):
    output = {}
    for i in a:
        for j in b:
            k = plus(i,j)
            if k in output:
                output[k] = (output[k] + 1) % 2
            else:
                output[k] = 1
    todel = []
    for i in output:
        if not output[i]:
            todel.append(i)
    for i in todel:
        del output[i]
    return output

ans = {(0,0):1}
while n > 0:
    if n & 1:
        ans = xor_product(terms, ans)
    n = n >> 1
    terms = xor_product(terms, terms)

a = 0
z = pow(2, pow(2, k, mod-1), mod)
for i in ans:
    a = (a + pow(z, i[0], mod) * pow(2, i[1], mod))%mod
print(a)