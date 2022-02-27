a, b = input().split()
a, b = int(a), int(b)
cand = []
flag = 0
cand.append(b * 4)
cand.append(b * 2)
cand.append(b)
cand.append(b / 2)
cand.append(b / 4)
for i in range(0, 3):
    weight = 0
    for j in range(0, 3):
        weight += cand[i+j]
    if(weight <= a):
        weight = int(weight*1000)
        print(weight)
        flag += 1
        break
if(flag == 0):
    print(0)