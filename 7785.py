n = int(input())
log = []
for i in range(n):
    temp = input().split()
    log.append(temp)

office = []
for i in log:
    if(i[1] == 'enter'):
        office.append(i[0])
    elif(i[1] == 'leave'):
        office.remove(i[0])
office.sort(reverse=True)
for i in office:
    print(i)