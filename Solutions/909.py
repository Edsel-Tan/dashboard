from prime import memoize

# Let R_k (f)(x) = f^k(x)
# S(R_k)(f)(x) = f(R_k(f)(x)) = f^(k+1)(x) which means S(R_k) = R_{k+1}
# S(Z)(f)(x) = f(x) => S(Z) = R_1
# S(S)(S(S))(S(S))(R_1)(A)(0) = S(S(S)) (S(S)) ( S ( S(S(S)) (S(S)) ) (R_1) ) (A) (0)
# Let R_k =  S ( S(S(S)) (S(S)) ) (R_1), then just need to evaluate S(S(S)) (S(S)) ( R_k ) (A) (0)

# Manually expand to get S(S) (R_k) = R_{k(k+1)}, S(S(S)) (R_k) = R_{k^2 * (k+1)}

@memoize
def S(u):
    @memoize
    def T(v):
        @memoize
        def U(w):
            return v(u(v)(w))
        return U
    return T

def Rk(k):
    def g(f):
        def h(x):
            for i in range(k):
                x = f(x)
            return x
        return h
    return g

A = lambda x: x+1

k = S ( S(S(S)) (S(S)) ) (Rk(1)) (A) (0)
f = lambda x: x*(x+1)
g = lambda x: x**2 * (x+1)
mod = 10**9
print(f(f(g(k))) % mod)