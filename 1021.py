n, m = map(int, input().split())
jimin_pick = list(map(int, input().split()))
ans = 0
que = []
for i in range(n):
    que.append(i+1)

for i in range(m):
    que_index = que.index(jimin_pick[i])
    if(que_index < len(que) - que_index):
        while(1):
            if(que[0] == jimin_pick[i]):
                del que[0]
                break
            else:
                que.append(que[0])
                del que[0]
                ans += 1
    else:
        while(1):
            if(que[0] == jimin_pick[i]):
                del que[0]
                break
            else:
                que.insert(0, que[-1])
                del que[-1]
                ans += 1

print(ans)