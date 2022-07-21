n, m = map(int, input().split())
original_boong = []
ans = []

for i in range(n):
    tmp = input()
    for j in range(m):
        print(tmp[m-j-1], end='')
    print()