n = int(input())
def p_star(num, max):
    print(' '*(max-num), end='')
    print('*'*num)
for i in range(1, n+1):
    p_star(i, n)
for i in range(1, n):
    p_star(n-i, n)