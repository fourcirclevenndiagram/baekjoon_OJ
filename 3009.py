dot = []
ans = []
for i in range(0, 3):
    a, b = input().split()
    dot.append((int(a), int(b)))
    dot.append((0, 0))
    print(dot)
for i in range(0, 3):
    for j in range(0, 3):
        if(dot[i][0] == dot[j][0]):
            dot[1][0] += 1
        if(dot[i][1] == dot[j][1]):
            dot[1][1] += 1
for i in range(0, 3):
    if(dot[1][0] == 1):
        ans.append(dot[1][0])
    if(dot[1][1] == 1):
        ans.append(dot[1][1])
print(ans[0], ans[1])