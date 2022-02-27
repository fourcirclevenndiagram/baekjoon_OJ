import sys
n = int(sys.stdin.readline())
ans = [0] * 10000000
for i in range(n):
    ans[i] = int(sys.stdin.readline())
for i in range(n):
    for j in range(n-i-1):
        if(ans[j] > ans[j+1]):
            ans[j], ans[j+1] = ans[j+1], ans[j]
for i in range(n):
    print(ans[i])