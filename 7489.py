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
        
for i in range(0, t):
    print(ans[i]%10)

# 런타임 에러 (OverflowError)
