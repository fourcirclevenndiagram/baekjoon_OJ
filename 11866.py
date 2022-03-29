import sys
n, k = map(int, sys.stdin.readline().split())
drawer = []
ans = []
idx = -1
real_idx = idx % k
for i in range(1, n+1):
    drawer.append(i)
while(drawer):
    idx += k
    # real_idx = idx % len(drawer)
    idx = idx % len(drawer)
    temp = drawer.pop(idx)
    ans.append(temp)
    idx -= 1
    
print("<", end = '')
for i in range(len(ans)-1):
    print("%d,"%ans[i], end = ' ')
if(len(ans) == 1):
    print("%d>"%ans[0])
else:
    print("%d>"%ans[i+1])