n, m = map(int, input().split())
my_b = []
your_b = []

for i in range(n):
    tmp = list(map(int, input().split()))
    my_b.append(tmp)

for i in range(n):
    tmp = list(map(int, input().split()))
    your_b.append(tmp)

for i in range(n):
    for j in range(m):
        print(my_b[i][j] + your_b[i][j], end=' ')
    print()