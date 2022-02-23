n = int(input())
for i in range(0, n):
    try:
        a, b = input().split()
        a, b = int(a), int(b)
        if((a > 0 and a < 10) and (b > 0 and b < 10)):
            print(a+b)        
    except:
        exit()
    