n = int(input())

a, b = 0, 1
i = 0
if(n == 1):
    print(0)
elif(n == 2):
    print(1)
else:
    for i in range(1, n):
        a, b = b, a+b
    print(b)