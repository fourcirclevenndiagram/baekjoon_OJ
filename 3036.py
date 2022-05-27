n = int(input())
drawer = list(map(int, input().split()))

def gcd(a, b):
    while(b != 0):
        c = a % b
        a = b
        b = c
    return a

for i in range(1, n):
    g = gcd(drawer[0], drawer[i])
    print("%d/%d"%(drawer[0]//g, drawer[i]//g))