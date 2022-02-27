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
        temp = n//C**i
        n -= temp*(C**i)
        temp = str(temp)
        ans.append(temp)
        i = 0
        if(n == 0):
            break
               

# ans.append(str(n))
ans = ''.join(ans)
ans = int(ans)
print(ans)