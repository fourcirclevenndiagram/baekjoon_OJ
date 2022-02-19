up = input().split()
down = input().split()
flag = 'Y'
for i in range(0, 5):
    if(up[i] == down[i]):
        flag = 'N'
        break
print(flag)