a, b = map(int, input().split())
tot = 0
drawer = []
for i in range(50):
    for j in range(i):
        drawer.append(i)
tot = sum(drawer[a-1:b])
print(tot)