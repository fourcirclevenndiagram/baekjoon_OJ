n = []
for i in range(0, 9):
    a = input()
    n.append(int(a))
max = n[0]
max_idx = 1
for i in range(1, 9):
    if(n[i] > max):
        max = n[i]
        max_idx = i+1
print(max)
print(max_idx)