n = 0
while(n > 0):
    n = input()
    n = int(n)
    i = 1
    drawer = []
    while(n > 1):
        if(n % i == 0):
            drawer.append(i)
            i += 1
