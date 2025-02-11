with open("0042_words.txt", 'r') as file:
    data = file.read().replace('"','').split(",")

max_len = max([len(i) for i in data]) * 26
s = set()
for i in range(1,max_len+1):
    x = (i*(i+1))//2
    if x > max_len:
        break
    s.add(x)

ans = 0
for i in data:
    c = 0
    for j in i:
        c += ord(j) - ord('A') + 1
    if c in s:
        ans += 1
print(ans)
