n,m = map(int,input().split())
board = []
size_max = 1

for i in range(n):
    board.append(list(input()))

for i in range(n):
    for j in range(m):
        for k in range(size_max, 50):
            if n <= (i+k) or m <= (j+k):
                break
            if len(set([board[i][j], board[i+k][j], board[i][j+k], board[i+k][j+k]])) == 1:
                size_max = max(size_max, k+1)

print(size_max**2)