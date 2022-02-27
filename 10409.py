a, b = map(int, input().split())
c = list(map(int, input().split()))
tot = 0
flag = 0
for i in range(0, a):
    c[i] = int(c[i])
    tot += c[i]
    if(tot > b):
        flag = 1
        break
if(flag):    
    print(i)
else:
    print(a)
