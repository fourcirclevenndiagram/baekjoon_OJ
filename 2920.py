a = input().split()
for i in range(0, 8):
    a[i] = int(a[i])
asc = 0
des = 0
for i in range(1, 8):
    if(a[i]>a[i-1]):
        asc += 1
    elif(a[i]<a[i-1]):
        des += 1
if(asc == 7):
    print("ascending")
elif(des == 7):
    print("descending")
else:
    print("mixed")