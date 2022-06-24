a = int(input())
cnt = 0

while(1):
    if(a == 0):
        break
    if(a%2 == 1):
        cnt += 1
    a //= 2

print(cnt)