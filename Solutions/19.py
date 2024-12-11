import datetime

ans = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        d = datetime.datetime(i, j, 1)
        if d.strftime("%A") == "Sunday":
            ans += 1
print(ans)