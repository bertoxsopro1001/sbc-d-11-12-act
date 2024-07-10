wlist = ["A", "B", "E", "Z", "X"]

for x in range(len(wlist)):
    for i in range(len(wlist) - x - 1): 
        if wlist[i] > wlist[i + 1]:
            temp = wlist[i]
            wlist[i] = wlist[i + 1]
            wlist[i + 1] = temp

print(wlist)
