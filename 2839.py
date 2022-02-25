n = int(input())
max_cnt = n // 3 + 1
flag = 0
ans = 0
for i in range(max_cnt):
    for j in range(max_cnt-i):
        if(n == i*3 + j*5):
            ans = i+j
            flag = 1
            break
    if(flag):
        print(ans)
        break
if(not flag):
    print(-1)