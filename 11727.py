n = int(input())
a, b = 1, 3
while(1):
    if(n == 1):
        print(1)
        break
    elif(n == 2):
        print(3)
        break
    else:
        for i in range(1, n):
            a, b = b, a*2+b
        print(a % 10007)
        break
