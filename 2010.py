import sys

n = int(sys.stdin.readline())
ans = 0

for i in range(n):
    tmp = int(input())
    ans += tmp

ans += 1-n 
print(ans)