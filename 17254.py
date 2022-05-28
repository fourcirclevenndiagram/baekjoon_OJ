n,m = map(int, input().split())
drawer = []

for i in range(m):
    a,b,c = input().split()
    a,b = int(a), int(b)
    c = str(c)
    drawer.append([a,b,c])

drawer.sort(key=lambda x: [x[1],x[0]])
# [ print(drawer[i][2], end='') for i in range(len(drawer)) ]
for i in range(m):
    print(drawer[i][2], end='')