n = input()
n = int(n)
i = 0
max = 1
while(1):
    i += 1
    if(n <= max):
        break
    max = max + (i*6)    
print(i)