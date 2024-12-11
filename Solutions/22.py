import math

with open('p022_names.txt','r') as file:
    txtnames = file.readlines()

txtnames = txtnames[0].replace("\"","").split(",")

txtnames = sorted(txtnames)

converter = {}

for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    converter[i] = ord(i) - 64
    
def conv(string):
    s = 0
    for c in string:
        s += converter[c]
    return s

total = 0
for i in range(len(txtnames)):
    total += (i+1) * conv(txtnames[i])
print(total)