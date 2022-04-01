n = int(input())
drawer = n
tmp = drawer
ans = 0
while(1):
    tmp = (drawer//10 + drawer%10) % 10
    drawer = (drawer%10)*10 + tmp
    if(drawer == n):
        break
    ans += 1
print(ans)