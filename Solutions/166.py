

def checkB(board):
    for row in board:
        for ele in row:
            if ele < 0 or ele > 9:
                return False
            
    rowsum = sum(board[0])
    for row in board:
        if sum(row) != rowsum:
            return False
    
    d1, d2 = 0, 0
    for i in range(4):
        s = 0
        d1 += board[i][i]
        d2 += board[3-i][i]
        for j in range(4):
            s += board[j][i]
        if s != rowsum:
            return False
    if d1 != rowsum or d2 != rowsum:
        return False
    return True

def check(x):
    return x < 0 or x > 9

# testboard = [[6,3,3,0],[5,0,4,3],[0,7,1,4],[1,2,4,5]]
# print(check(testboard))

ans = 0


for a1 in range(10):
    for a2 in range(10):
        for a3 in range(10):
            for a4 in range(10):
                m = a1 + a2 + a3 + a4
                # print("m: ", m)
                for a6 in range(10):
                    for a10 in range(10):
                        a14 = m - a2 - a6 - a10
                        # print("a14: ", a14, a2, a6, a10)
                        if check(a14):
                            continue
                        # print("a14!: ", a14, a2, a6, a10)
                        for a7 in range(10):
                            a11 = m - a6 - a7 - a10
                            if check(a11):
                                continue
                            a13 = m - a4 - a7 - a10
                            if check(a13):
                                continue
                            a14 = m - a2 - a6 - a10
                            if check(a14):
                                continue
                            a15 = m - a3 - a7 - a11
                            if check(a15):
                                continue
                            a16 = m - a1 - a6 - a11
                            if check(a16):
                                continue
                            for a5 in range(10):
                                a8 = m - a5 - a6 - a7
                                if check(a8):
                                    continue
                                a9 = m - a1 - a5 - a13
                                if check(a9):
                                    continue
                                a12 = m - a9 - a10 - a11
                                if check(a12):
                                    continue
                                # if not checkB([[a1,a2,a3,a4],[a5,a6,a7,a8],[a9,a10,a11,a12],[a13,a14,a15,a16]]):
                                #     print("HUH?!")
                                # print([a1,a2,a3,a4],[a5,a6,a7,a8],[a9,a10,a11,a12],[a13,a14,a15,a16], sep="\n")
                                # print("-----")
                                ans += 1

print(ans)

        
    
    