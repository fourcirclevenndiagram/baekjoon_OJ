import math
x, y = map(int, input().split())
z = math.trunc(y/x*100) + 1
if(x == y):
    print(-1)
else:
    i = 0
    while((y/x*100) < z):
        x += 1
        y += 1
        i += 1
    print(i)