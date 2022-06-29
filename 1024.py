n, l = map(int, input().split())
drawer = []

def solve(length, n):
    x = n - (int(length * (length+1) // 2))
    return x / length

for i in range(l, 101):
    a = solve(i, n)
    if int(a) == a:
        a = int(a)
        tmp = sum(range(a+i+1)) - sum(range(a+1))
        if tmp == n:
            drawer = (list(range(a+1, a+i+1)))
            drawer = list(map(str, drawer))
            break

if 0 < len(drawer) <= 100:
    print(' '.join(drawer))
else:
    print(-1)