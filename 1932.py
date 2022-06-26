n = int(input())
drawer = []
for i in range(n):
    tmp = list(map(int, input().split()))
    drawer.append(tmp)

for i in range(1, n):
    for j in range(i+1):
        if(j == 0):
            drawer[i][j] = drawer[i][j] + drawer[i-1][j]
        elif(i == j):
            drawer[i][j] = drawer[i][j] + drawer[i-1][j-1]
        else:
            drawer[i][j] = max(drawer[i][j] + drawer[i-1][j], drawer[i][j] + drawer[i-1][j-1])

print(max(drawer[n-1]))