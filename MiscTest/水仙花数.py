from math import pow

s=[]

for i in range(100, 1000):
    baiwei = int(i/100)
    shiwei = int((i-100*baiwei)/10)
    gewei = int(i-100*baiwei-10*shiwei)

    if (i == pow(baiwei,3) + pow(shiwei,3) + pow(gewei,3)):
        s.append(i)
        i = i+1
    else:
        i = i + 1

print(s)

