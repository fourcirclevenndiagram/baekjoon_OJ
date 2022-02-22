n = input()
n = int(n)
flag = []
for i in range(0, n):

    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    if(a**2 + b**2 == c**2):
        flag.append(1)
    else:
        flag.append(0)
for i in range(0, n):
    if(flag[i]):
        print("Scenario #%d:"%(i+1))
        print("yes")
    else:
        print("Scenario #%d:"%(i+1))
        print("no")
    if(i < n-1):
        print()