n = 24
mid = 2**(n-1)
r = mid**2

def check(x, y):
    return (x-mid)**2 + (y-mid)**2 <= r

def checkSquares(sqs):
    for i in range(len(sqs)-1):
        if check(*sqs[i]) != check(*sqs[i+1]):
            return False
    return True

ans = 1
stack = [((0,0), 2**(n-1)), ((2**(n-1),0), 2**(n-1)), ((0,2**(n-1)), 2**(n-1)), ((2**(n-1),2**(n-1)), 2**(n-1))]
while len(stack) > 0:
    top = stack[-1]
    del stack[-1]
    
    sqs = [top[0], 
           (top[0][0] + top[1] - 1, top[0][1]),
           (top[0][0], top[0][1] + top[1] - 1),
           (top[0][0] + top[1] - 1, top[0][1] + top[1] - 1)]
    
    # print(sqs)
    
    if checkSquares(sqs):
        ans += 2

    else:
        ans += 1
        stack.append((top[0], top[1]//2))
        stack.append(((top[0][0] + top[1]//2, top[0][1]), top[1]//2))
        stack.append(((top[0][0], top[0][1] + top[1]//2), top[1]//2))
        stack.append(((top[0][0] + top[1]//2, top[0][1] + top[1]//2), top[1]//2))

print(ans)
