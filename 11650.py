n = int(input())
drawer = []
for i in range(n):
    x, y = map(int, input().split())
    drawer.append((x,y))
drawer.sort(key=lambda x: (x[0], x[1]))
for i in range(n):
    print(drawer[i][0], drawer[i][1])