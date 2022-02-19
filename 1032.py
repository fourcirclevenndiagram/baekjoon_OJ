t = input()
t = int(t)
cmd_stg = []
for i in range(0, t):
    cmd = input()
    cmd_stg.append(cmd)
if(t == 0):
    print(cmd_stg[0])
elif(t > 0):
    ans = list(cmd_stg[0])
    for i in range(1, t):
        for j in range(0, len(ans)):
            if(ans[j] != cmd_stg[i][j]):
                ans[j] = '?'
    print(''.join(map(str, ans)))
    