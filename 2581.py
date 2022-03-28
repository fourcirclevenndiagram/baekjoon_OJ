m = int(input())
n = int(input())
prime_num = []
ans = 0
for i in range(m, n+1):
    flag = 0
    if(i > 1):
        for j in range(2, i):
            if(not (i%j)):
                flag = 1
                break
        if(not flag):
            prime_num.append(i)

if(len(prime_num) == 0):
    print(-1)
else:
    for i in prime_num:
        ans += i
    print(ans)
    print(prime_num[0])