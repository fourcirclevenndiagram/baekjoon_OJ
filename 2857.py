drawer = []
flg = 0
for i in range(5):
    drawer.append(input())

for i in range(len(drawer)):
    if "FBI" in drawer[i]:
        print(i+1, end=' ')
        flg += 1

if not flg:
    print('HE GOT AWAY!')