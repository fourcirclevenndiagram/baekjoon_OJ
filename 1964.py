n = int(input())
ans = 5
pl = 7

for i in range(1, n):
    ans += pl
    pl += 3

print(ans % 45678)