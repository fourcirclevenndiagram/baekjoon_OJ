a = input().split()
tot = 0
for i in range(0, 5):
    a[i] = int(a[i])
    tot += a[i]**2
print(tot%10)
