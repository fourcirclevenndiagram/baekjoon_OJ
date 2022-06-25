drawer = []
for i in range(5):
    drawer.append(int(input()))
drawer = sorted(drawer)
idx = len(drawer) // 2
print(int(sum(drawer) / 5))
print(drawer[idx])