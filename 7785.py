import sys
n = int(sys.stdin.readline())
log = []
for i in range(n):
    temp = sys.stdin.readline().split()
    log.append(temp)

office = []
for i in log:
    if(i[1] == 'enter'):
        office.append(i[0])
    elif(i[1] == 'leave'):
        office.remove(i[0])
# office.sort(reverse=True)
ans = sorted(office, reverse=True)
for i in ans:
    print(i)