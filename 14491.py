n = input()
n = int(n)
k = n
ans = []
while(1):
    C = 1
    i = 0
    while(1):
        C *= 9
        if(n > C):
            i += 1
            continue
        C /= 9
        


ans.append(str(n))
ans = ''.join(ans)
ans = int(ans)
print(ans)