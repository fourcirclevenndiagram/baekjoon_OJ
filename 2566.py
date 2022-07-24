drawer = []

for i in range(9):
    tmp = list(map(int, input().split()))
    drawer.append(tmp)

x, y = 0, 0
max = 0

for i in range(9):
    for j in range(9):
        if drawer[i][j] > max:
            max = drawer[i][j]
            x, y = i+1, j+1

print(max)
print(x, y)