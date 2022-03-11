import sys

for i in range(0, 3):
    n = int(sys.stdin.readline())
    tot = 0
    for j in range(0, n):
        temp = int(sys.stdin.readline())
        tot += temp
    if(tot == 0):
        print(0)
    elif(tot > 0):
        print("+")
    else:
        print("-")
        
