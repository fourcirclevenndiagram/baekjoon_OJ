a = input().split()
x, y, r = input().split()
shock = 0
for i in range(0, 4):
    if(a[i] == x):
        print(i+1)
        shock = 1
if(shock == 0):
    print(0)