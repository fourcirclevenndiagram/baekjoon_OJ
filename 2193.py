drawer = [0, 1, 1]
for i in range(88):
    drawer.append(drawer[i+1] + drawer[i+2])
n = int(input())
print(drawer[n])