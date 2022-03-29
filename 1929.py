m, n = map(int, input().split())
prime_lst = []
for i in range(m, n+1):
    flag = 0
    for j in range(2, i):
        if(i%j == 0):
            flag = 1
            break
    if(not flag):
        prime_lst.append(i)
print(prime_lst)
    