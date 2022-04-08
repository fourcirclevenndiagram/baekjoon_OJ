m = int(input())
n = int(input())
drawer = []
i = 1

while(1):
    if(i**2 > n):
        break
    if(m <= i**2 <= n):
        drawer.append(i**2)
    i += 1

if(len(drawer)):
    print(sum(drawer))
    print(drawer[0])
else:
    print(-1)