tmp = input()
cnt = 0
r = 1
c = len(tmp)
org_c = c

for i in range(1, org_c+1):
    if(org_c%i == 0):
        if(r < i and i <= org_c//i):
            r = i
            c = org_c//i

drawer = [[] for i in range(r)]

for i in range(c):
    for j in range(r):
        drawer[j].append(tmp[cnt])
        cnt += 1

for i in range(r):
    print(''.join(drawer[i]), end='')