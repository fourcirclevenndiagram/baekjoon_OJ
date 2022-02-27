while(1):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    max = a
    p1, p2 = b, c
    if(b > max):
        if(c > b):
            max = c
            p1, p2 = a, b
        else:
            max = b
            p1, p2 = a, c
    if(not(a > 0 and b > 0 and c > 0)):
        break
    if(p1**2 + p2**2 == max**2):
        print("right")
    else:
        print("wrong")