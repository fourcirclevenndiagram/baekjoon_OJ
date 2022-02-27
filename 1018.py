b, a = input().split()
b, a = int(b), int(a)

given_board = []
for i in range(0, b):
    given_board.append(input())

def scan(x, y, board, key_word):
    count = 0
    if(key_word == 'W'):
        for i in range(y, y+8):
            for j in range(x, x+8):
                if((i+j)%2 == 0 and board[i][j] == 'B'):
                    count += 1
                if((i+j)%2 == 1 and board[i][j] == 'W'):
                    count += 1
    elif(key_word == 'B'):
        for i in range(y, y+8):
            for j in range(x, x+8):
                if((i+j)%2 == 0 and board[i][j] == 'W'):
                    count += 1
                if((i+j)%2 == 1 and board[i][j] == 'B'):
                    count += 1
    return count
            
scan_range_x = a - 7
scan_range_y = b - 7
min_work = 64
for i in range(0, scan_range_y):
    for j in range(0, scan_range_x):
        print(j, i, given_board[i][j])
        temp = scan(j, i, given_board, given_board[i][j])
        if(temp < min_work):
            min_work = temp

print(min_work)