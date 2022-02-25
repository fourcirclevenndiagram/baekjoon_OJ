n = int(input())
cnt = 0
if(n < 100):
    print(n)
elif(100 <= n and n <= 1000):
    while(n >= 100):
        n = str(n)
        if(ord(n[0])-ord(n[1]) == ord(n[1])-ord(n[2])):
            cnt += 1
        n = int(n)
        n -= 1
    print(99+cnt)