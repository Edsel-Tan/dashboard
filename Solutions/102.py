def sl(lis):
    output = 0

    for i in range(-1,len(lis) - 1):
        output += lis[i][0] * lis[i+1][1] - lis[i][1] * lis[i+1][0]

    return output

def check(lis):
    p = lis[:3]
    q = lis[1:]
    r = [lis[0],lis[1],lis[3]]
    s = [lis[0],lis[2],lis[3]]

    return abs(sl(p)) == abs(sl(q)) + abs(sl(r)) + abs(sl(s))

with open('p102_triangles.txt','r') as file:
    tri = file.readlines()

count = 0
for i in tri:
    l = i.strip('\n').split(',')
    for i in range(len(l)):
        l[i] = int(l[i])
    l = [(l[0],l[1]),(l[2],l[3]),(l[4],l[5]),(0,0)]
    
    if check(l):
        count += 1
print(count)