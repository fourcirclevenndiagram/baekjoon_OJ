a= input().split()
isHereEven = 0
isHereOdd = 0
oddClub = []
ans = 1
for i in range(0, 3):
    a[i] = int(a[i])
    if(a[i] % 2 == 0):
        isHereEven += 1
    if(a[i] % 2 == 1):
        isHereOdd += 1
        oddClub.append(a[i])

if(isHereEven > 0 and isHereOdd > 0):
    for i in range(0, len(oddClub)):
        ans *= oddClub[i]
else:
    for i in range(0, len(a)):
        ans *= a[i]
print(ans)