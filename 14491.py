n = input()
n = int(n)
k = n
ans = []
while(n > 9):
    C = 9
    i = 0
    while(n > C):
        C *= 9
        i += 1
    ans.append(str(n//(9**i)))
    n = n % (9**i)
ans.append(str(n))
ans = ''.join(ans)
ans = int(ans)
print(ans)