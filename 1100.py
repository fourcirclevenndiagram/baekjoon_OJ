board = []
count = 0
for i in range(0, 8):
    n = input()
    n = list(n)
    board.append(n)
for i in range(0, 8):
    for j in range(0, 8):
        if((i+j)%2 == 0 and board[i][j] == 'F'):
            count += 1
print(count)