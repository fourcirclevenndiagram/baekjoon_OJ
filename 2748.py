n = int(input())
drawer_f = []
num = 0

for i in range(n+1):
    len_f = len(drawer_f)
    if i == 0:
        num = 0
    elif i <= 2:
        num = 1
    else:
        num = drawer_f[-1] + drawer_f[-2]
    drawer_f.append(num)

print(drawer_f[-1])