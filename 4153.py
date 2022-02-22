while(1):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if(not(a > 0 and b > 0 and c > 0)):
        break
    if(a**2 + b**2 == c**2):
        print("right")
    else:
        print("wrong")