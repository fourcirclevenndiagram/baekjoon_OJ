n = int(input())
drawer = []

for i in range(n):
    drawer.append(int(input()))

drawer = sorted(drawer)
for i in range(len(drawer)):
    print(drawer[i])