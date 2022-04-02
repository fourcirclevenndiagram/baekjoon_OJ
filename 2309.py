height = []
flag = 0
for i in range(9):
    height.append(int(input()))

for i in range(9):
    for j in range(i+1, 9):
        if(sum(height) - height[i] - height[j] == 100):
            t1, t2 = height[i], height[j]
            height.remove(t1)
            height.remove(t2)
            flag = 1
            break
    if(flag):
        break

if(flag):
    height.sort()
    for i in height:
        print(i)