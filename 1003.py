p0, p1 = 0, 0
print("t값을 받습니다")
t = input()
t = int(t)

def fibo(n):
    if(n == 0):
        print("0")
        p0 += 1
        return 0
    elif(n == 1):
        print("1")
        p1 += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(0, t):
    p0, p1 = 0, 0
    print("m값을 받습니다")
    m = input()
    m = int(m)
    fibo(m)
    print(p0, p1)