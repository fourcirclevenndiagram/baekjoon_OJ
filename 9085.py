t = int(input())
for i in range(0, t):
    n = int(input())
    a = input().split()
    tot = 0
    for j in range(0, n):
        a[j] = int(a[j])
        tot += a[j]
    print(tot)
        