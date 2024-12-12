import math
from sieve import pf
import itertools

def deg(P):
    return max(P.keys())

def multiply(P, Q):
    coeff = {}

    for i in P.keys():

        for j in Q.keys():

            if i+j in coeff.keys():
                coeff[i+j] += P[i] * Q[j]
            else:
                coeff[i+j] = P[i] * Q[j]

    zeros = []
    for i in coeff.keys():
        if coeff[i] == 0:
            zeros.append(i)
    for i in zeros:
        del coeff[i]

    return coeff

def add(P,Q):
    coeff = P.copy()

    for i in Q.keys():
        if i in coeff.keys():
            coeff[i] += Q[i]
        else:
            coeff[i] = Q[i]

    zeros = []
    for i in coeff.keys():
        if coeff[i] == 0:
            zeros.append(i)
    for i in zeros:
        del coeff[i]

    return coeff

def sub(P,Q):
    coeff = P.copy()

    for i in Q.keys():
        if i in coeff.keys():
            coeff[i] -= Q[i]
        else:
            coeff[i] = -Q[i]

    zeros = []
    for i in coeff.keys():
        if coeff[i] == 0:
            zeros.append(i)
    for i in zeros:
        del coeff[i]

    return coeff

def divide(P, Q):
    coeff = P.copy()
    degP = deg(coeff)
    degQ = deg(Q)

    output = {}
    while degP >= degQ:
        if coeff[degP] % Q[degQ] != 0:
            return False

        q = coeff[degP] // Q[degQ]
        d = degP - degQ

        coeff = sub(coeff, multiply({d:q}, Q))

        output[d] = q
        
        if len(coeff.keys()) == 0:
            break
        degP = max(coeff.keys())

    zeros = []
    for i in output.keys():
        if output[i] == 0:
            zeros.append(i)
    for i in zeros:
        del output[i]
    return output, coeff
    
def cyclotomic(n):
    """Returns nth cyclotomic polynomial"""
    pfs = pf(n)
    coeffs = {1:1, 0:-1}
    for p in pfs:

        ###Applying first p
        coeffs_temp = {}
        for i in coeffs.keys():
            coeffs_temp[p[0]*i] = coeffs[i]
        coeffs, remainder = divide(coeffs_temp, coeffs)
        if remainder != {}:
            print("Error generating cyclotomic polynomial!")


        ###Applying subsequent ps
        if p[1] > 1:
            coeffs_temp = {}
            for i in coeffs.keys():
                coeffs_temp[p[0]**(p[1]-1)*i] = coeffs[i]
            coeffs = coeffs_temp
   
        
    return coeffs

def count(P, k):
    """Returns the sum of coefficients of x^n where n < k, given coefficients of P are {0,1}"""
    output = 0
    for i in range(k):
        if i in P.keys():
            output += 1
    return output

##Too slow. Works for all examples
##n = 36
##cn = cyclotomic(n)
##k = 6
##
##polynomials = [({0:0},{0:0})]
##for i in range(n-deg(cn)):
##    polynomials_temp = []
##    print(i, len(polynomials))
##    
##    for P,Q in polynomials:
##        
##        if i > k:
##            if count(Q, i) > k:
##                continue
##
##        if i in Q.keys():
##            qi = Q[i]
##        else:
##            qi = 0
##
##        for j in range(2):
##            pi = j - qi
##        
##            p = {i:pi}
##            q = multiply(p, cn)
##            polynomials_temp.append((add(P,p), add(Q,q)))
##
##    polynomials = polynomials_temp
##
##polynomials_temp = []
##for P, Q in polynomials:
##    count = 0
##    for i in Q.keys():
##        if Q[i] != 0 and Q[i] != 1:
##            break
##        count += Q[i]
##    else:
##        if count == k:
##            polynomials_temp.append((P,Q))
##polynomials = polynomials_temp


##Attempt 2
import time

n = 30
cn = cyclotomic(n)
k = 20
run = True
#dubious_bound = 1000

modcn = {}
imodcn = {}
for i in range(n):
    modcn[i] = divide({i:1},cn)[1]
    m = min(modcn[i].keys())
    if m in imodcn.keys():
        imodcn[m][modcn[i][m]].append((i, modcn[i]))
    else:
        imodcn[m] = [[],[],[]]
        imodcn[m][modcn[i][m]].append((i, modcn[i]))
    #print(modcn[i])


if run:
    polynomials = {(0,(),()):1}
    for i in sorted(list(imodcn.keys())):
        lt = time.time()
        #print(list(polynomials.keys())[:10])
        
        polynomials_temp = {}
        for count,pk,pv in polynomials.keys():
            P = dict(zip(pk,pv))
            choices = k - count
            choices = min(choices, len(imodcn[i][1]) * 2)#, dubious_bound)

            if i in P.keys():
                pi = P[i]
            else:
                pi = 0

            parity = pi%2

            for r in range(parity,choices+1,2):
                #pos + neg = -pi, pos - neg = r,
                pos = (-pi+r)//2
                neg = -(-pi-r)//2
                if pos < 0 or neg < 0:
                    continue
                for s1 in itertools.combinations(imodcn[i][1], pos):
                    for s2 in itertools.combinations(imodcn[i][2],neg):
                        p = {}
                        for j in s1:
                            p = add(p,j[1])
                        for j in s2:
                            p = add(p,j[1])

                        if count+r <= k:
                            q = add(p,P)
                            qk = tuple(q.keys())
                            qv = tuple(q.values())
                            key = (count+r, qk, qv)
                            if key in polynomials_temp.keys():
                                polynomials_temp[key] += polynomials[(count,pk,pv)]
                            else:
                                polynomials_temp[key] = polynomials[(count,pk,pv)]


                            
                
##                for s in itertools.combinations(imodcn[i], r):
##                    
##                    p = {}
##                    for j in s:
##                        p = add(p, j[1])
##                        
##                    if i in p.keys():
##                        c = p[i]
##                    else:
##                        c = 0
##                        
##                    if c == -pi:
##                        if count + r <= k:
##                            q = add(p,P)
##                            qk = tuple(q.keys())
##                            qv = tuple(q.values())
####                            if math.ceil(len(qk)) + count + r <= k:
##                            key = (count+r, qk, qv)
##                            if key in polynomials_temp.keys():
##                                polynomials_temp[key] += polynomials[(count,pk,pv)]
##                            else:
##                                polynomials_temp[key] = polynomials[(count,pk,pv)]

        polynomials = polynomials_temp

        pass
    



##with open("idata.txt","w+") as file:   
##    for i in imodcn.keys():
##        for j in imodcn[i]:
##            file.write(str(i) + " " + str(j) + "\n")
##
##
##        
##with open("data.txt","w+") as file:   
##    for i in modcn.keys():
##        file.write(str(i) + " " + str(modcn[i]) + "\n")

p = {}
for i in polynomials.keys():
    p[i[0]] = polynomials[i]

np = p.copy()
for i in range(11):
    a = list(np.keys())
    np_temp = dict(zip(a, [0 for i in a])) 
    for i in p.keys():
        for j in np.keys():
            if i + j <= k:
                np_temp[i+j] += p[i] * np[j]
    np = np_temp

print(np[20])


        

        
        

        


                
