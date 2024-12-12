from math import exp, inf

def f(st):
    ans = 0
    for i in range(1, len(st)):
        ans += exp(-st[i-1]) * st[i]
    return ans

def g(x):
    start = 0
    end = 10**10
    st = [0]
    while x < end:
        st.append(x)
        if x <= start:
            return inf
        if x - start > 100:
            break
        x, start = exp(x - start), x
    # print(st)
    return f(st)

l = 0
r = 3
eps = 1e-12
while (r-l) > eps:
    m1 = l + (r-l)/3
    m2 = r - (r-l)/3
    if g(m1) > g(m2):
        l = m1
    else:
        r = m2

print("{:.9f}".format(g(r)))
# print(l, g(0.4))

# # print(g(0.7))