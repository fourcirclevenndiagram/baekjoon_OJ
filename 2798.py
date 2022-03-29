n, m = map(int, input().split())
drawer = list(map(int, input().split()))
ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            keep_card = drawer[i]+drawer[j]+drawer[k]
            if(keep_card > m):
                continue
            else:
                ans = max(ans, keep_card)

print(ans)