s = input()
s = int(s)

total = 0
seed = 1
n = 0
while(1):
    total += seed
    seed += 1
    n += 1
    if(total > s):
        print(n-1)
        break
    