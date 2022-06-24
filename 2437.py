n = int(input())
drawer = sorted(list(map(int, input().split())))
ans = 1

for num in drawer:
    if(num > ans):
        break
    ans += num

print(ans)