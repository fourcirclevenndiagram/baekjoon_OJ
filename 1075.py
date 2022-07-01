n = int(input())
f = int(input())
ans = (n // 100) * 100

while(1):
    if ans%f == 0:
        break
    ans += 1
print(str(ans)[-2:])