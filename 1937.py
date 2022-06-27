import sys
sys.setrecursionlimit(10**7)

n = int(input())
ans = 0
board = [list(map(int,input().split())) for i in range(n)]
dp = [[-1]*n for i in range(n)]
mv = [(0,1),(1,0),(0,-1),(-1,0)]

def solve(x, y):
    if(dp[x][y] == -1):
        dp[x][y] = 0
        for a,b in mv:
            dx = x + a
            dy = y + b
            if(n>dx>=0 and n>dy>=0 and board[x][y]<board[dx][dy]):
                dp[x][y] = max(dp[x][y], solve(dx,dy))
    return dp[x][y]+1

for i in range(n):
    for j in range(n):
        ans = max(ans, solve(i, j))
            
print(ans)