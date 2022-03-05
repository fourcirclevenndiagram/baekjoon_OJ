n = int(input())
for i in range(1, n+1):
    if(i%2 == 0):
        print(' ', end='')
    for j in range(1, (n*2)+1):
        if(j%2 == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print()

    