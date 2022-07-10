while 1:
    n = input()
    drawer = []
    tot = 0
    if n == '0':
        break
    for i in n:
        drawer.append(i)
    for i in drawer:
        tot += 1
        if i == '0':
            tot += 4
        elif i == '1':
            tot += 2
        else:
            tot += 3

    print(tot+1)