n = 9898
mod = 989898989

ans = 0

def add(x):
    global ans
    ans = (ans + 2*x) % mod

#Multiply answer by two to handle case where all gold coins are silver and vice versa
#Gold coin referred to as 2, silver coin referred to as 1

#Case 1: c 2s, a 1s, b 1s, c = a+b
#Case 1.1: Nothing else
#b + c = i

for c in range(2, n+1):
    #Multiply 3 for each position of c 2s
    add(3 * (c-1))

#Case 1.1.1: padding extra 1,2 pairs
for c in range(2, n+1):
    #Multiply 3 for each position of c 2s
    add(3 * (c-1) * (pow(2,n-c+1, mod) - 2))

#Case 1.2: extra thriplets
dp_0 = [0,0]

curr_state = {1:[1,0]}
for i in range(2, n):
    new_state = {}
    for j in curr_state:
        #Add 122
        if j-1 not in new_state:
            new_state[j-1] = [0,0]
        new_state[j-1][1] = (new_state[j-1][1] + curr_state[j][0] + 3 * curr_state[j][1]) % mod

        #Add 211
        if j+1 not in new_state:
            new_state[j+1] = [0,0]
        new_state[j+1][0] = (new_state[j+1][0] + curr_state[j][1] + 3 * curr_state[j][0]) % mod
    if 0 in new_state:
        dp_0.append(sum(new_state[0]))
    else:
        dp_0.append(0)
    curr_state = new_state

cumulative_dp_0 = [0]
for i in range(1, n):
    cumulative_dp_0.append((cumulative_dp_0[-1] + dp_0[i]) % mod)

"""dp_1 = [0,0]

curr_state = {1:1}
for i in range(2, n):
    new_state = {}
    for j in curr_state:
        #Add 122
        if j-1 not in new_state:
            new_state[j-1] = 0
        new_state[j-1] = (new_state[j-1] + curr_state[j]) % mod

        #Add 211
        if j+1 not in new_state:
            new_state[j+1] = 0
        new_state[j+1] = (new_state[j+1] + curr_state[j]) % mod
    if 0 in new_state:
        dp_1.append(new_state[0])
    else:
        dp_1.append(0)
    curr_state = new_state

cumulative_dp_1 = [0]
for i in range(1, n):
    cumulative_dp_1.append((cumulative_dp_1[-1] + dp_1[i]) % mod)"""


#Case 1.2.1: bigger thriplets at a
for c in range(2, n):
    #Multiply 3 for each position of c 2s. Multiply 2 to choose empty slot of last column.
    add(3 * 2 * (c-1) * cumulative_dp_0[n-c-1])
    """
    #Possible overcount
    add(-3 * 2 * (c-1) * cumulative_dp_1[n-c-1])
    """


#Case 1.2.1.1: padding extra 1,2 pairs
for c in range(2, n):
    #Multiply 3 for each position of c 2s. Multiply 2 to choose empty slot of last column.
    for x in range(n-c-1):
        add(3 * 2 * (c-1) * (dp_0[x]) * (pow(2, n-(c+x+1)+1, mod) - 2))



#Case 1.2.2: bigger thriplets not at a
for c in range(2, n+1):
    #Multiply 3 for each position of c 2s.
    add(3 * (c-1) * cumulative_dp_0[n-c])
    """
    #Possible overcount
    add(-3 * (c-1) * cumulative_dp_1[n-c])
    """

#Case 1.2.2.1: padding extra 1,2 pairs
for c in range(2, n+1):
    #Multiply 3 for each position of c 2s.
    for x in range(n-c+1):
        if c % 2 == 0:
            d = c//2
            add(3 * 2 * (dp_0[x] * (pow(2, n-(d+1+x+1)+2, mod) - pow(2, n-(c-1+x+1)+1, mod))))
            add(3 * dp_0[x] * pow(2, n-(d+x+1)+1, mod))
            add(3 * dp_0[x] * (-2) * (c-1))
        else:
            d = c//2 + 1
            add(3 * 2 * (dp_0[x] * (pow(2, n-(d+x+1)+2, mod) - pow(2, n-(c-1+x+1)+1, mod))))
            add(3 * dp_0[x] * (-2) * (c-1))

        """for b in range(1, c):
            add(3 * (dp_0[x]) * (pow(2, n-(max(b, c-b)+x+1)+1, mod) - 2))"""


#Case 2: c 2s, a 1s, b 1s, c = a + b + 1
#Case 2.1: extra thriplets

dp_0 = [0,0]

curr_state = {-3:[0,1]}
for i in range(2, n):
    new_state = {}
    for j in curr_state:
        #Add 122
        if j-1 not in new_state:
            new_state[j-1] = [0,0]
        new_state[j-1][1] = (new_state[j-1][1] + curr_state[j][0] + 3 * curr_state[j][1]) % mod

        #Add 211
        if j+1 not in new_state:
            new_state[j+1] = [0,0]
        new_state[j+1][0] = (new_state[j+1][0] + curr_state[j][1] + 3 * curr_state[j][0]) % mod
    if -1 in new_state:
        dp_0.append(sum(new_state[-1]))
    else:
        dp_0.append(0)
    curr_state = new_state

cumulative_dp_0 = [0]
for i in range(1, n):
    cumulative_dp_0.append((cumulative_dp_0[-1] + dp_0[i]) % mod)

"""dp_1 = [0,0]

curr_state = {-3:1}
for i in range(2, n):
    new_state = {}
    for j in curr_state:
        #Add 122
        if j-1 not in new_state:
            new_state[j-1] = 0
        new_state[j-1] = (new_state[j-1] + curr_state[j]) % mod

        #Add 211
        if j+1 not in new_state:
            new_state[j+1] = 0
        new_state[j+1] = (new_state[j+1] + curr_state[j]) % mod
    if -1 in new_state:
        dp_1.append(new_state[-1])
    else:
        dp_1.append(0)
    curr_state = new_state

cumulative_dp_1 = [0]
for i in range(1, n):
    cumulative_dp_1.append((cumulative_dp_1[-1] + dp_1[i]) % mod)"""

#Case 2.1.1: bigger thriplets at a
for c in range(2, n):
    #Multiply 3 for each position of c 2s. Multiply 2 to choose empty slot of last column.
    add(3 * 2 * (c-1) * cumulative_dp_0[n-c])


old = ans
#Case 2.1.1.1: extra 1,2 padding
for c in range(2, n):
    #Multiply 3 for each position of c 2s. Multiply 2 to choose empty slot of last column.
    for x in range(n-c):
        add(3 * 2 * (c-1) * (dp_0[x]) * (pow(2, n-(c+x)+1, mod) - 2))


#Case 2.1.2: bigger thriplets not at a
if n >= 2:
    add(3 * cumulative_dp_0[n-2])

for c in range(3, n):
    #Multiply 3 for each position of c 2s.
    add(3 * (c-3) * cumulative_dp_0[n-c+1])
    add(3 * 2 * cumulative_dp_0[n-c])

old = ans
#Case 2.1.2.1: extra 1,2 padding
for c in range(2, n):
    #Multiply 3 for each position of c 2s
    for x in range(n-c+1):
        if c % 2 == 0:
            d = c//2
            add(3 * 2 * (dp_0[x] * (pow(2, n-(d+1+x+1)+2, mod) - pow(2, n-(c-1+x+1)+1, mod))))
            add(3 * dp_0[x] * pow(2, n-(d+x+1)+1, mod))
            add(3 * dp_0[x] * (-2) * (c-1))
        else:
            d = c//2 + 1
            add(3 * 2 * (dp_0[x] * (pow(2, n-(d+x+1)+2, mod) - pow(2, n-(c-1+x+1)+1, mod))))
            add(3 * dp_0[x] * (-2) * (c-1))

        """for b in range(1, c):
            add(3 * (dp_0[x]) * (pow(2, n-(max(b, c-b)+x+1)+1, mod) - 2))"""
        
    x = n-c+1
    for b in range(2, c-1):
        add(3 * (dp_0[x]) * (pow(2, n-(max(b, c-b)+x+1)+1, mod) - 2))


print(ans%mod)