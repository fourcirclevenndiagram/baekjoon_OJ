n = int(input())
ans = 0
for a in range(1, n):
    for b in range(1, a+1):
        if(a**2 - b**2 == n):
            ans += 1
print(ans)