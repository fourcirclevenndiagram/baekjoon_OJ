a = input()
idx = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
for i in range(0, 26):
    for j in range(0, len(a)):
        if(i == ord(a[j])-97):
            idx[i] = j
            break
            
for i in range(0, 26):
    print("%d "%idx[i], end = '')