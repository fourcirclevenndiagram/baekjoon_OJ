import sys
m, n = map(int, sys.stdin.readline().split())
prime_lst = []
for i in range(m, n+1):
    flag = 0
    for j in range(2, int(i**0.5)+1):
        if(i%j == 0):
            flag = 1
            break
    if(not flag):
        prime_lst.append(i)
for i in prime_lst:
    print(i)
    