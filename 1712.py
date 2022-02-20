a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
i = 0
while(1):
    i += 1
    if(a+(b*i) < c*i):
        break
print(i)

# 시간초과