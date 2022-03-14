'''
import sys

p0, p1 = 0, 0
t = -1
while(t < 0 or t > 40):
 print("t값을 받습니다")
# t = input()
 t = sys.stdin.readline()
 t = int(t)

def fibo(n):
    global p0, p1
    if(n == 0):
        # print("0")
        p0 += 1
        return 0
    elif(n == 1):
        # print("1")
        p1 += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(0, t):
    p0, p1 = 0, 0
    print("m값을 받습니다")
    # m = input()
    m = sys.stdin.readline()
    m = int(m)
    fibo(m)
    print(p0, p1)
'''

import sys
t = int(sys.stdin.readline())

for i in range(t):
    a = int(input())
    p0, p1 = 0, 1
    if(a == 0):
        print("1 0")
        continue
    elif(a == 1):
        print("0 1")
        continue
    for j in range(a-1):
        p0, p1 = p1, p0+p1
    print(p0, p1)