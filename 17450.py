i = 0
best_gsb = -1
pre_gsb = -1
gsb = 0
while(i < 3):
    a, b = input().split()
    a, b = int(a), int(b)
    gsb = b/a    
    if(i > 0 and gsb == pre_gsb):
        i -= 1
        continue
    if(gsb > pre_gsb):
        best_gsb = i
    pre_gsb = gsb    
    i += 1
if(best_gsb == 0):
    print('S')
elif(best_gsb == 1):
    print('N')
elif(best_gsb == 2):
    print('U')