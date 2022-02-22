t = input()
t = int(t)

ans = []
for i in range(0, t):
    n = input()
    n = int(n)
    for j in range(1, n):
        n *= j
    while(n%10 == 0):
        n /= 10
    ans.append(n)
for i in range(0, t):
    print(int(ans[i]%10))

# 런타임 에러 (OverflowError)
