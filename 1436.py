n = int(input())
cnt = 0
name = '666'
created_name = 660
flag = 0
while(1):
    created_name += 1
    if(name in str(created_name) and not flag):
        cnt += 1
        if(cnt == n):
            print(created_name)
            flag = 1
            break
