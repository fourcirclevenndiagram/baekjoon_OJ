n, m = map(int, input().split())
drawer = []
for i in range(n+1):
    drawer.append([0]*(m+1))
drawer[1][1] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        dx = j + 1
        dy = i + 1
        if(0 < dx <= m and 0 < dy <= n):
            drawer[dy][dx] += drawer[i][j]
        if(0 < dx <= m):
            drawer[i][dx] += drawer[i][j]
        if(0 < dy <= n):
            drawer[dy][j] += drawer[i][j]
            
print(drawer[n][m] % 1000000007)