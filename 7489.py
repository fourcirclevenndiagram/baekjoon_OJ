t = input()
t = int(t)

ans = []
for i in range(0, t):
    n = input()
    n = int(n)
    if(n == 0):
        ans.append(1)
        break
    for j in range(1, n):
        n *= j
        if(n%10 == 0):
            n /= 10     
    ans.append(n)
for i in range(0, t):
    print(int(ans[i]%10))

# 런타임 에러 (ValueError)
