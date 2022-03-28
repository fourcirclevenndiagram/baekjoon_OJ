import sys
input = sys.stdin.readline
n = int(input())
x = list(map(int, input().split()))
# ans = []
worked_x = sorted(list(set(x)))
# for i in x:
#     cnt = 0
#     for j in worked_x:
#         if(i > j):
#             cnt += 1
#     ans.append(cnt)
ans = {worked_x[i] : i for i in range(len(worked_x))}

for i in x:
    print(ans[i], end=' ')
