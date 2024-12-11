from decimal import Decimal #type: ignore
import decimal # type: ignore
decimal.getcontext().prec = 30

def multiply(P, Q):
    output = [0 for i in range(len(P) + len(Q) - 1)]
    for i in range(len(P)):
        for j in range(len(Q)):
            output[i+j] += P[i] * Q[j]
    return output
    
def add(P, Q):
    output = [0 for i in range(max(len(P), len(Q)))]
    for i in range(len(P)):
        output[i] += P[i]
    for i in range(len(Q)):
        output[i] += Q[i]
    return output

def multiply2(P, Q):
    output = [[0] for i in range(len(P) + len(Q) - 1)]
    for i in range(len(P)):
        for j in range(len(Q)):
            output[i+j] = add(output[i+j], multiply(P[i], Q[j]))
    return output


ans = [[1]]
for x in range(1, 51):
    p = [[0,x],[1, -x]]
    ans = multiply2(ans, p)

def evaluate(P, x):
    output = 0
    c = 1
    for i in P:
        output += c * i
        c *= x
    return output

P = ans[20]
lower = Decimal(50)
upper = Decimal(60)

while upper-lower > 10**(-12):
    middle = (upper+lower)/2
    if evaluate(P, 1/middle) > 0.02:
        lower = middle
    else: 
        upper = middle

print("{:.10f}".format(upper))
