while(1):
    n = input()
    n = int(n)
    if(n == -1):
        break
    k = n
    tot = 0
    i = 2
    drawer = []
    drawer.append(1)
    if(n == 1):
        print("1 is NOT perfect")
        continue
    while(i < n/2+1):
        if(n % i == 0):
            drawer.append(i)
            i += 1
        else:
            i += 1
    for i in range(0, len(drawer)):
        tot += drawer[i]
    if(n != tot):
        print("%d is NOT perfect"%k)
    elif(n == tot):
        print("%d = "%tot, end='')
        for i in range(0, len(drawer)-1):
            print("%d + "%drawer[i], end='')
        print("%d"%drawer[i+1])