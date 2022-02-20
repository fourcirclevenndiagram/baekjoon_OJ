t = input()
t = int(t)
for i in range(0, t):
    n = input()
    n = int(n)
    k = n
    drawer = []
    max = 0
    if(k == 1):
        print(1)
        continue
    while(n != 1):
        drawer.append(n)
        if(n%2 == 0):
            n /= 2
        else:
            n = n*3 + 1
    max = drawer[0]      

    for j in range(1, len(drawer)):
        if(drawer[j] > drawer[j-1]):
            max = drawer[j]
    max = int(max)
    print(max)

# 시간 초과