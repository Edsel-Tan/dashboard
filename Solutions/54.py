with open('p054_poker.txt','r') as file:
    pokerhands = file.readlines()

cardstrength = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

hands = []
for hand in pokerhands:
    hands.append(hand.replace("\n",""))


def score(hand):
    ranks = '23456789TJQKA'
    rcounts = {ranks.find(r): ''.join(hand).count(r) for r, _ in hand}.items()
    score, ranks = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])
    if len(score) == 5:
        if ranks[0:2] == (12, 3): #adjust if 5 high straight
            ranks = (3, 2, 1, 0, -1)
        straight = ranks[0] - ranks[4] == 4
        flush = len({suit for _, suit in hand}) == 1
        '''no pair, straight, flush, or straight flush'''
        score = ([(1, ), (3,1,1,1)], [(3,1,1,2), (5,)])[flush][straight]
    return score, ranks

def poker(hands):
    scores = [(i, score(hand.split())) for i, hand in enumerate(hands)]
    #print(scores)
    winner = sorted(scores , key=lambda x:x[1])[-1][0]
    return winner

p1win = 0
for hand in hands:
    if poker([hand[:14],hand[15:]]) == 0:
        p1win += 1
    
print(p1win)