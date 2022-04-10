drawer = []
for i in range(10):
    n = int(input())
    drawer.append(n % 42)

print(len(set(drawer)))

