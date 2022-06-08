while(1):
    n = input()
    n = int(n)
    ans = ''
    if(n == -1):
        break
    k = n
    tot = 0
    i = 2
    drawer = []
    drawer.append(1)
    if(n == 1):        
        print("1 is NOT perfect.")
        continue
    if(n == 0):
        print("0 is NOT perfect.")
        continue
    while(i < n):
        if(n % i == 0):
            drawer.append(i)
            i += 1
        else:
            i += 1
    for i in range(0, len(drawer)):
        tot += drawer[i]
    if(n != tot):
        # print("%d is NOT perfect"%k)
        ans += "%d is NOT perfect."%k
    elif(n == tot):
        # print("%d = "%tot, end='')
        ans += "%d = "%tot
        for i in range(0, len(drawer)-1):
            # print("%d + "%drawer[i], end='')
            ans += "%d + "%drawer[i]
        # print("%d"%drawer[i+1])
        ans += "%d"%drawer[i+1]
    print(ans)