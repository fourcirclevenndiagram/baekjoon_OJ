n = int(input())
lst = list(map(int, input().split()))
drawer = []
ans = 0

drawer.append(lst[0])
for i in range(1, n):
    drawer.append(drawer[i-1] + lst[i])
for i in range(n):
    ans += lst[i] * (drawer[n-1] - drawer[i])
print(ans)