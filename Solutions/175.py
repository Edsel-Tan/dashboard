# Question is kinda poggers but one assumption gonna be made
# Do the obvious recursion important part is to rewrite it.
# Represent each binary string as (ai, bi) ai 1s followed by bi 0s, ok for ai bi to be 0
# A_i+1 = (a_i * b_i + 1) * A_i + a_i * B_i
# B_i+1 = b_i * A_i + B_i
# Is the rewriting of the big recurrence. Which can be made into an obvious matrix multiplication.
# Notice that when we allow ai bi to be 0 it inspires us to break the matrix into smaller components.
# Now (Ai Bi) is just a gcd.
# Now big assumption is that f(n) and f(n-1) have gcd 1.

import math

f_n = 13717421
f_n_1 = 109739369


def calculate(sbf):
    a = 1
    b = 0
    for i in range(len(sbf)-1, -1, -1):
    # while len(sbf) != 0:
        if i % 2 == 1:
            b = sbf[i] * a + b
        else:
            a = a + sbf[i] * b
    
    return a, b

def subtract(sbf):
    sbf = sbf.copy()
    if len(sbf) % 2 == 1:
        # print("ZZ")
        if sbf[-1] == 1:
            sbf[-2] += 1
            del sbf[-1]
        else:
            sbf[-1] -= 1
            sbf.append(1)
        return sbf

    if sbf[-2] == 1:
        if len(sbf) == 2:
            sbf[0] = sbf[-1]
            del sbf[-1]
        else:
            sbf[-3] += 1
            sbf[-2] = sbf[-1]
            del sbf[-1]
    else:
        sbf[-2] -= 1
        sbf.append(sbf[-1])
        sbf[-2] = 1
    return sbf

for i in range(1, f_n):
        
    if math.gcd(f_n, i) != 1:
        continue

    sbf = []

    a = f_n
    b = i
    while b != 1:
        sbf.append(a//b)
        a = a % b
        c = a
        a = b
        b = c
    
    if len(sbf) % 2 == 1:
        # sbf.append(a-1)
        # sbf.append(1)
        sbf.append(a//b)
    else:
        # sbf.append(a//b)
        sbf.append(a-1)
        sbf.append(1)

    ss = sbf.copy()
    sbf.append(0)
    while calculate(subtract(sbf))[0] < f_n_1:
        sbf[-1] += 1

    if calculate(subtract(sbf))[0] == f_n_1:
        print(",".join([str(i) for i in sbf]))
        break



    