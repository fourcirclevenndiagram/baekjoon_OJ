t = input()
t = int(t)

for i in range(0, t):
    a = input().split()
    a[0] = float(a[0])
    for j in range(1, len(a)):
        if(a[j] == '@'):
            a[0] *= 3
        elif(a[j] == '%'):
            a[0] += 5
        elif(a[j] == '#'):
            a[0] -= 7
    print("%.2f"%a[0])
