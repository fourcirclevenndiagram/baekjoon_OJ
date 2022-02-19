t = input()
t = int(t)
a, b, c = 0, 0, 0
while(t >= 300):
    a += 1
    t -= 300
while(t >= 60):
    b += 1
    t -= 60
while(t >= 10):
    c += 1
    t -= 10
if(t==0):
    print(a, b, c)
else:
    print(-1)