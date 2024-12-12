"""
There are 81C3 = 85320 sets of 3 cards, say A1, A2, ..., A85320. Let Si = 1 if
Ai is a set, Si = 0 otherwise.

Then S(Cn)^4 = (Si + Sj + ...) ** 4 is a polynomial in Si.

We attempt to calculate parts of this polynomial
E.g. sum(Si^2 * Sj * Sk) where |Ai U Aj U Ak| = r

"""
import math
import sys
import time
sys.setrecursionlimit(2000)
def C(n,r):
    output = 1
    for i in range(r):
        output *= n-i
    for i in range(r):
        output = int(output/(i+1))
    return output

#constants

answers = {}
###Case 1: 1 distinct sets, coeff = 1
answers[1] = {3:1080}

###Case 2: 2 distinct sets, coeff = 4+6+4 = 14
###4 is impossible

#Subcase 1: 5 distinct eles
#Choose common node, 40C2 ways to choose node pairs
b1 = 81 * 20 * 39

#Subcase 2: 6 distinct eles
#Subtract case 2, note that there are only 2 sets among these 6 points
#(81C3)C2
b2 = 540 * 1079 - b1

answers[2] = {5:b1*14, 6: b2*14}

###Case 3: 3 distinct sets, coeff = 12+12+12 = 36
###5 is impossible

#Subcase 1: 6 distinct eles
#2 non-intersecting set = die
#Exist 5 ele 2 set, 4C2 = 10 ways to choose pair
c1 = 4 * int(b1/3)

#Subcase 2: 7 distinct eles
c2 = 9 * b2 + 38 * int(b1/3)

#Subcase 3: 8 distinct eles
c3 = b2 * 3 * 36

#Subcase 4: 9 distinct eles
c4 = 180 * 1079 * 1078 - c1 - c2 - c3
answers[3] = {6: c1*36, 7:c2*36, 8:c3*36, 9:c4*36}

#Case 4: coeff = 24

#Subcase 1: 12 eles
answers[4] = {7: 210600*24, 8: 23060700*24, 9: 629641350*24, 10: 5911626240*24,
              12: 27791899200*24, 11: 22016208240*24}

n=12
output = 0
for i in range(1,5):
    for j in range(3,n+1):
        if j in answers[i].keys():
            output += C(81-j, n-j) * answers[i][j]
            # print(output)
print(output)
