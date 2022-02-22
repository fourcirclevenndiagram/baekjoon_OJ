n = input()
n = int(n)
a = input().split()
a[0] = int(a[0])
max = min = a[0]
for i in range(1, n):
    a[i] = int(a[i])
    if(max < a[i]):
        max = a[i]
    elif(min > a[i]):
        min = a[i]
print(min, max)