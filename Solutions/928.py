from math import comb
from prime import memoize
from itertools import product

@memoize
# hand from 1 to 6
def fifteen_first(hand):
    s = {0:1}
    for i in range(len(hand)):
        for _ in range(hand[i]):
            ns = s.copy()
            for j in s:
                k = i + j + 1
                if k > 15:
                    continue
                if k not in ns:
                    ns[k] = 0
                ns[k] += s[j]
            s = ns
    return s

@memoize
# hand from 7 to K
def fifteen_last(hand):
    s = {0:1}
    for i in range(len(hand)):
        for _ in range(hand[i]):
            ns = s.copy()
            for j in s:
                k = j + min(i + 7, 10)
                if k > 15:
                    continue
                if k not in ns:
                    ns[k] = 0
                ns[k] += s[j]
            s = ns
    return s

def fifteen(hand):
    first = hand[:6]
    last = hand[6:]
    sf = fifteen_first(first)
    sl = fifteen_last(last)
    s = {}
    for i in sf:
        for j in sl:
            k = i + j
            if k > 15:
                continue
            if k not in s:
                s[k] = 0
            s[k] += sf[i] * sl[j]
    return s


def cribbage(hand):
    output = 0

    for i in hand:
        output += comb(i, 2) * 2
    
    rl = 0
    nr = 1
    for i in hand:

        if i:
            rl += 1
            nr *= i
        else:
            if rl >= 3:
                output += rl * nr
            rl = 0
            nr = 1
        
    if rl >= 3:
        output += rl * nr
    
    s = fifteen(hand)
    if 15 in s:
        output += s[15] * 2
    return output

def h(hand):
    output = 0
    for i in range(len(hand)):
        output += hand[i] * min(i+1, 10)
    return output

def next_permutation(hand):
    l = list(hand)
    idx = len(hand) - 1
    while idx >= 0 and l[idx] == 4:
        l[idx] = 0
        idx -= 1
    if idx < 0:
        return False
    l[idx] += 1
    return tuple(l)

def est_first(hand):
    output = 0

    for i in hand:
        output += comb(i, 2) * 2
    
    rl = 0
    nr = 1
    for i in hand:

        if i:
            rl += 1
            nr *= i
        else:
            if rl >= 3:
                output += rl * nr
            rl = 0
            nr = 1
        
    if rl >= 3:
        output += rl * nr
    
    s = fifteen_first(hand)
    if 15 in s:
        output += s[15] * 2
    return output

def est_last(hand):
    output = 0

    for i in hand:
        output += comb(i, 2) * 2
    
    rl = 0
    nr = 1
    for i in hand:

        if i:
            rl += 1
            nr *= i
        else:
            if rl >= 3:
                output += rl * nr
            rl = 0
            nr = 1
        
    if rl >= 3:
        output += rl * nr
    
    s = fifteen_last(hand)
    if 15 in s:
        output += s[15] * 2
    return output

ans = 0
done = 0
mx = 4 * sum([min(i+1, 10) for i in range(13)]) + 1

pos_last_hands = []
last = tuple([0 for i in range(7)])
while last:
    if est_last(last) < mx:
        pos_last_hands.append(last)
    last = next_permutation(last)

pos_first_hands = []
first = tuple([0 for i in range(6)])
while first:
    if est_first(first) < mx:
        pos_first_hands.append(first)
    first = next_permutation(first)

total = len(pos_first_hands)

for first in pos_first_hands:
    done += 1
    for last in pos_last_hands:
        hand = first + last
        if h(hand) == cribbage(hand):
            x = 1
            for c in hand:
                x *= comb(4, c)
            ans += x
print(ans-1)