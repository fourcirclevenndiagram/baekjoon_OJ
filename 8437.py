a = int(input())
b = int(input())
ans = 0
for i in range(a):
    if(ans*2 + b == a):
        break
    ans += 1
print(ans+b, ans)