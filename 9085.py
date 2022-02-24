t = int(input())
for i in range(0, t):
    n = int(input())
    a = map(int, input.split())
    tot = 0
    for j in range(0, n):
        tot += a[j]
    print(tot)
        