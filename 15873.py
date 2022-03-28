n = list(input())
ans = 0
for i in n:
    ans += int(i)
    if(i == '0'):
        ans += 9
print(ans)