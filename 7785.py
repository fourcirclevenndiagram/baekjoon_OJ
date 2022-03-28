import sys
n = int(sys.stdin.readline())
office = {}
for i in range(n):
    name, cmd = sys.stdin.readline().split()
    if(cmd == 'enter'):
        office[name] = 'inOffice'
    elif(cmd == 'leave'):
        del office[name]
       
# office.sort(reverse=True)
ans = sorted(office, reverse=True)
for i in ans:
    print(i)